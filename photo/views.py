
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, redirect, HttpResponseRedirect, get_object_or_404,render
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from Ms.settings import MEDIA_URL
from models import *
from forms import *
from datetime import datetime
from django.core.mail import send_mail
from Ms.local_settings import EMAIL_HOST_USER
# coding: utf-8
def God(request):
    categories_list = Categories.objects.all()
    images_filtered_list = Image.objects.all().filter(approved=True)
    last_photos_list = images_filtered_list.filter(created=datetime.today())
    args = {}
    args.update(csrf(request))
    paginator = Paginator(images_filtered_list, 7)
    try:
        page = int(request.GET.get("page", '1'))
    except ValueError:
        page = 1
    try:
        images = paginator.page(page)
    except (InvalidPage, EmptyPage):
        images = paginator.page(paginator.num_pages)
    args['categories'] = categories_list
    args['images'] = images
    args['user'] = request.user
    args['media_url'] = MEDIA_URL
    args['last'] = last_photos_list
    return render_to_response("base.html", args)


# TODO: REWORK LOGIN SYSTEM, BUG WITH SESSIONS ON OTHER PAGES
@login_required()
# TODO: Broken SHIT
def addPhoto(request):
    args = {}
    args.update(csrf(request))
    form = PhotoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        img = form.save(commit=False)
        img.user = request.user
        img.save()
        form.save_m2m()
        return HttpResponseRedirect(reverse('addPhoto'))
    args['form']=form
    return render_to_response('addphoto.html', args)


def addlike(request, img_id):
    if img_id:
        image = get_object_or_404(Image, id=img_id)
        ifliked = image.liked_persons.filter(username=request.user).exists()
        if not ifliked:
            image.liked_persons.add(request.user)
            image.likes += 1
            image.save()
        else:
            image.liked_persons.remove(request.user)
            image.likes -= 1
            image.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def show_your_pictures(request):
    args = {}
    image_list = Image.objects.all().filter(user=request.user)
    da = image_list.filter(created=datetime.today())
    args['image'] = image_list
    args['da'] = da
    return render_to_response('ypic.html', args)


def image(request, id):
    img = get_object_or_404(Image,id=id)
    args = {}
    args.update(csrf(request))
    args['form'] = ImageChangeForm()
    args['user'] = request.user
    args['image'] = img
    args['backurl'] = request.META.get("HTTP_REFERER")
    args['media_url'] = MEDIA_URL
    return render_to_response('image.html', args)


def update(request,id=None):
    instance = get_object_or_404(Image, id=id)
    form = ImageChangeForm(request.POST or None, instance=instance)
    if form.is_valid():
        img = form.save(commit=False)
        img.save()
        #messages.success(request, "Updated")
        return HttpResponseRedirect('/')#TODO: Make an absolute url to models and rewrite this shit
    context = {
            "instance": instance,
            "form": form
        }
    return render(request,'update.html',context)


def categories_detail(request, cat_pk):
    categories_list = get_object_or_404(Categories,pk=cat_pk)
    images_list = categories_list.images.all()
    if not request.user.is_authenticated():
        images_list = images_list.filter(approved=True)
    args = {}
    args.update(csrf(request))
    args['cat'] = categories_list
    args['images'] = images_list
    args['backurl'] = request.META.get("HTTP_REFERER")
    args['media_url'] = MEDIA_URL
    args['user'] = request.user
    return render_to_response('categories_detail', args)


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        subject = 'HALP'
        contact_massage = form.cleaned_data.get('text')
        from_email = EMAIL_HOST_USER
        to_email = [form.cleaned_data.get('email')]
        send_mail(subject,
                  contact_massage,
                  from_email,
                  to_email,
                  fail_silently=False)
        # for key,value in form.cleaned_data.iteritems():
        #     print key,value
    context = {'form': form}
    return render(request, 'cus.html', context)
#TODO: test it on any other environment
def delete(request,id=None):
    instance = get_object_or_404(Image, id=id)
    os.remove(instance.image.path)
    instance.delete()
    #TODO: need to change it on album reverse absolute ulr, i think
    return redirect('/')