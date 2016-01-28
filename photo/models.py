from django.db import models
from taggit.managers import TaggableManager
from django.core.files import File
from django.contrib.auth.models import User
from tempfile import NamedTemporaryFile
from string import join
import os
from PIL import Image as PImage
from Ms.settings import MEDIA_ROOT
# -*- coding: utf-8 -*-
class Image(models.Model):
    title = models.CharField(max_length=60)
    image = models.ImageField(upload_to="images/", verbose_name="Image")
    user = models.ForeignKey(User, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    width = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    thumbnail2 = models.ImageField(upload_to="media/", blank=True, null=True)
    liked_persons = models.ManyToManyField(User, related_name='follows', symmetrical=False, blank=True)
    likes = models.IntegerField(default=0)
    approved = models.BooleanField(default=False)
    tags = TaggableManager()
    def __unicode__(self):
        return self.image.name

    def thumbnail(self):
        return """<a href="/media/%s"><img border="0" alt="" src="/media/%s" height="40" /></a>""" % (
            (self.image.name, self.image.name))

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

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
    def size(self):
        """Image size."""
        return "Width:%s x Height:%s" % (self.width, self.height)
    def tags_(self):
        lst = [x[1] for x in self.tags.values_list()]
        return str(join(lst, ','))
    thumbnail.allow_tags = True


class Categories(models.Model):
    title = models.CharField(max_length=200)
    images = models.ManyToManyField(Image)

    def __unicode__(self):
        return self.title
    def get_images(self):
        return "\n".join([p.title for p in self.images.all()])