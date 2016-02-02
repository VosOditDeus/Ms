from django.db import models
from taggit.managers import TaggableManager
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
from django.contrib.auth.models import User
from string import join
# -*- coding: utf-8 -*-
def upload_location(instance,filename):
    return "%s/%s" % (instance.user, filename)
class Image(models.Model):
    title = models.CharField(max_length=60)
    image = models.ImageField(upload_to=upload_location,
                              verbose_name="Image",
                              width_field='width_field',
                              height_field='heigth_field')
    width_field = models.IntegerField(default=0)
    heigth_field = models.IntegerField(default=0)
    user = models.ForeignKey(User, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    liked_persons = models.ManyToManyField(User, related_name='follows', symmetrical=False, blank=True)
    likes = models.IntegerField(default=0)
    approved = models.BooleanField(default=False)
    tags = TaggableManager()
    def __unicode__(self):
        return self.image.name

    def thumbnail(self):
        return """<a href="/media/%s"><img border="0" alt="" src="/media/%s" height="40" /></a>""" % (
            (self.image.name, self.image.name))
    # def save(self, *args, **kwargs):
    #     """Save image dimensions."""
    #     super(Image, self).save(*args, **kwargs)
    #     im = PImage.open(os.path.join(MEDIA_ROOT, self.image.name))
    #     self.width, self.height = im.size
    #      # large thumbnail
    #     fn, ext = os.path.splitext(self.image.name)
    #     im.thumbnail((128,128), PImage.ANTIALIAS)
    #     thumb_fn = fn + "-thumb2" + ext
    #     tf2 = NamedTemporaryFile()
    #     im.save(tf2.name, "JPEG")
    #     self.thumbnail2.save(thumb_fn, File(open(tf2.name)), save=False)
    #     tf2.close()
    #     super(Image, self).save(*args, ** kwargs)
    def tags_(self):
        lst = [x[1] for x in self.tags.values_list()]
        return str(join(lst, ','))
    thumbnail.allow_tags = True
#TODO: can be bugs with POST delete, check it up.
@receiver(pre_delete,sender=Image)
def image_post_delete_handler(sender, **kwargs):
    image = kwargs['instance']
    storage, path = image.image.storage, image.image.path
    storage.delete(path)

class Categories(models.Model):
    title = models.CharField(max_length=200)
    images = models.ManyToManyField(Image)

    def __unicode__(self):
        return self.title
    def get_images(self):
        return "\n".join([p.title for p in self.images.all()])