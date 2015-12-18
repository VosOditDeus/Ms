from django.shortcuts import render_to_response, redirect,HttpResponse,Http404,HttpResponseRedirect,get_object_or_404
#from django.views.generic import View
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone

from Ms.settings import MEDIA_URL
from models import *
from forms import *
# coding: utf-8
"""
Class-based views
class God(View):

    def get(self, request):
        form = CommentForm(request.POST)
        args = {}
        args.update(csrf(request))
        args['image'] = Image.objects.all()
        args['form'] = form
        args['username']=auth.get_user(request).username
        #args['albums']=Album.objects.get(created_by=User)
        return render_to_response('base1.html', args)always go

    def post(self, request):
        pass
"""

def about(request):
    return render_to_response('about.html')


def God(request):
    albums = Album.objects.all()
    images = Image.objects.all()
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
    time = timezone._time.time()
    return render_to_response("base.html", dict(albums=albums, user=request.user,
                                                media_url=MEDIA_URL, images=images, time=time))

def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            args['user'] = auth.get_user(request)
            return redirect('/', args)
        else:
            args['login_error'] ="Not found"
            return render_to_response('main.html', args)

    else:
        return render_to_response('main.html', args)


def logout(request):
    auth.logout(request)
    return redirect('/')

def addComment(request, pk):
    if request.method=="POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.poste_to.get(pk=pk)
            comment.save()
            form.save()
    return redirect('/image/%s' % pk)
@login_required()
def addPhoto(request):
    args = {}
    args.update(csrf(request))
    if request.method == "POST":
        form = PhotoForm(request.POST, files=request.FILES)
        if form.is_valid():
            img = form.save(commit=False)
            img.user = request.user
            img.save()
            form.save_m2m()
            return redirect('/')
    else:
        form = PhotoForm()
        args['form'] = form
    return render_to_response('addphoto.html',args)


def album(request, pk):
    """Album listing."""
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
    print pk
    return render_to_response("album.html", dict(album=album, images=images, user=request.user,
                                                 media_url=MEDIA_URL))


def image(request, pk):
    """Image page."""
    img = Image.objects.get(pk=pk)
    return render_to_response("image.html", dict(image=img, user=request.user,
                                                 backurl=request.META["HTTP_REFERER"], media_url=MEDIA_URL))
#TODO:What the fuck is it, i honestly don't know, but i need this structure- List-albums-images-media_url


def addlike(request, img_id):
    print img_id
    try:
        if img_id in request.COOKIES:
            # TODO:Write NORMAL system to prevent likes abuse,that will WORK at least
            redirect('/')
            print img_id
        else:
            image = Image.objects.get(id=img_id)
            image.likes += 1
            image.save()
            responce = HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            responce.set_cookie(img_id, 'test cookie')
            print img_id
    except ObjectDoesNotExist:
        raise Http404
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
