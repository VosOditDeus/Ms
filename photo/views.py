from collections import defaultdict

from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, redirect,HttpResponse,HttpResponseRedirect,get_object_or_404,Http404
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from Ms.settings import MEDIA_URL
from models import *
from forms import *
# coding: utf-8
def God(request):
    albums = Album.objects.all().filter(approved=True)[:10]
    categories = Categories.objects.all()[:10]
    images = Image.objects.all()[:10]
    args = {}
    args.update(csrf(request))
    if not request.user.is_authenticated():
        albums = albums.filter(public=True)
    paginator = Paginator(albums, 2)
    try:
        page = int(request.GET.get("page", '1'))
    except ValueError:
        page = 1
    try:
        albums = paginator.page(page)
    except (InvalidPage, EmptyPage):
        albums = paginator.page(paginator.num_pages)

    for album in albums.object_list:
        album.images = album.image_set.all()
    args['albums']=albums
    args['categories']=categories
    args['images']=images
    args['user']=request.user
    args['media_url']=MEDIA_URL
    return render_to_response("base.html",args)
#TODO: REWORK LOGIN SYSTEM, BUG WITH SESSIONS
@login_required()
def addPhoto(request):
    args = {}
    args.update(csrf(request))
    if request.method == "POST":
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            img = form.save(commit=False)
            img.user = request.user
            img.save()
            form.save_m2m()
            return HttpResponseRedirect(reverse('addPhoto'))
        else:
            args['errors']=form.errors
            args['form'] = form
            return render_to_response('addphoto.html',args)
    else:
        form = PhotoForm()
        args['form'] = form
    return render_to_response('addphoto.html',args)
def album(request, pk):
    """Album listing."""
    #TODO: Bug - user must not  create albums with same name,create a widget in user albumaddform
    album = get_object_or_404(Album, pk=pk)
    if not album.public and not request.user.is_authenticated():
        return HttpResponse("Error: you need to be logged in to view this album.")

    images = album.image_set.all()
    paginator = Paginator(images, 30)
    try:
        page = int(request.GET.get("page", '1'))
    except ValueError:
        page = 1

    try:
        images = paginator.page(page)
    except (InvalidPage, EmptyPage):
        images = paginator.page(paginator.num_pages)
    return render_to_response("album.html", dict(album=album, images=images, user=request.user,
                                                 media_url=MEDIA_URL))
def addlike(request, img_id):
    if img_id:
        a=Image.objects.get(id=img_id)
        ifliked=a.liked_persons.filter(username=request.user).exists()
        if not ifliked:
            a.liked_persons.add(request.user)
            a.likes += 1
            a.save()
        else:
            a.liked_persons.remove(request.user)
            a.likes -= 1
            a.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
def show_your_albums(request):
    args= {}
    user=request.user
    alb = Album.objects.all().filter(created_by=user)
    img1 = Image.objects.filter(user=user).first()
    args['albums'] = alb
    #args['user'] = user
    args['image'] = img1
    return render_to_response('yalbums.html', args)

def image(request,id):
    img =Image.objects.get(id=id)
    album=Album.objects.all()
    args ={}
    args.update(csrf(request))
    args['form'] = ImageChangeForm()
    args['albums']=album
    args['user']=request.user
    args['image']=img
    args['backurl']=request.META.get("HTTP_REFERER")
    args['media_url']=MEDIA_URL
    return render_to_response('image.html', args)

def update(request):
    args = {}
    args.update(csrf(request))
    if request.method == "POST":
        form = ImageChangeForm(request.POST)
        if form.is_valid():
            img = form.save(commit=True)
            img.user = request.user
            img.save()
            form.save_m2m()
            return HttpResponseRedirect(reverse('update'))
        else:
            args['errors'] = form.errors
            args['form'] = form
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        form = ImageChangeForm()
        args['form'] = form
    return render_to_response('image.html', args)


def categories_detail(request,cat_pk):
    Cat=Categories.objects.get(pk=cat_pk)
    images = Cat.images.all()
    albums = Cat.albums.all()
    args ={}
    args.update(csrf(request))
    args['cat']=Cat
    args['images']=images
    args['albums']=albums
    args['backurl']=request.META.get("HTTP_REFERER")
    args['media_url']=MEDIA_URL
    return render_to_response('categories_detail',args)