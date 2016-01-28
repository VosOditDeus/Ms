from django.core.files.uploadedfile import UploadedFile
from django.core.urlresolvers import reverse
from django.http import HttpResponseBadRequest
from django.shortcuts import render_to_response, redirect, HttpResponse, HttpResponseRedirect, get_object_or_404,render
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.template import RequestContext
from sorl.thumbnail import get_thumbnail

from Ms import settings
from Ms.settings import MEDIA_URL
from models import *
from forms import *
from datetime import datetime
from django.core.mail import send_mail
from Ms.local_settings import EMAIL_HOST_USER
import simplejson

# coding: utf-8
def God(request):
    categories = Categories.objects.all()
    images = Image.objects.all().filter(approved=True)
    last_photos = images.filter(created=datetime.today())
    args = {}
    args.update(csrf(request))
    paginator = Paginator(images, 7)
    try:
        page = int(request.GET.get("page", '1'))
    except ValueError:
        page = 1
    try:
        images = paginator.page(page)
    except (InvalidPage, EmptyPage):
        images = paginator.page(paginator.num_pages)
    args['categories'] = categories
    args['images'] = images
    args['user'] = request.user
    args['media_url'] = MEDIA_URL
    args['last'] = last_photos
    return render_to_response("base.html", args)


# TODO: REWORK LOGIN SYSTEM, BUG WITH SESSIONS ON OTHER PAGES
@login_required()
# TODO: Broken SHIT
def addPhoto(request):
    args = {}
    args.update(csrf(request))
    if request.method == "POST":
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            img = form.save(commit=False)
            img.user = request.user
            # title = form.cleaned_data.get("title")
            # if not img.title:
            #     title = '#'
            # img.title = title
            img.save()
            form.save_m2m()
            return HttpResponseRedirect(reverse('addPhoto'))
        else:
            args['form'] = form
            return render_to_response('addphoto.html', args)
    else:
        form = PhotoForm()
        args['form'] = form
    return render_to_response('addphoto.html', args)


def addlike(request, img_id):
    if img_id:
        a = get_object_or_404(Image, id=img_id)
        ifliked = a.liked_persons.filter(username=request.user).exists()
        if not ifliked:
            a.liked_persons.add(request.user)
            a.likes += 1
            a.save()
        else:
            a.liked_persons.remove(request.user)
            a.likes -= 1
            a.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def show_your_pictures(request):
    args = {}
    img = Image.objects.all().filter(user=request.user)
    da = img.filter(created=datetime.today())
    args['image'] = img
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
        return HttpResponseRedirect('/')#TODO: Make an absolute url to models and rewrite this shit
    context={
            "instance": instance,
            "form": form
        }
    return render(request,'update.html',context)


def categories_detail(request, cat_pk):
    Cat = get_object_or_404(Categories,pk=cat_pk)
    images = Cat.images.all()
    if not request.user.is_authenticated():
        images = images.filter(approved=True)
    args = {}
    args.update(csrf(request))
    args['cat'] = Cat
    args['images'] = images
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
