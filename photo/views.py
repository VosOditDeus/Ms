from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.views.generic import View
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from Ms.settings import MEDIA_URL
from models import *
from forms import *

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
        return render_to_response('base1.html', args)

    def post(self, request):
        pass
"""
def God(request):
    albums=Album.objects.all()
    images=Image.objects.all()
    if not request.user.is_authenticated():
        albums=albums.filter(public=True)
    paginator = Paginator(albums, 1)
    try:
        page = int(request.GET.get("page", '1'))
    except ValueError: page = 1
    try:
        albums = paginator.page(page)
    except (InvalidPage, EmptyPage):
        albums = paginator.page(paginator.num_pages)

    for album in albums.object_list:
        album.images = album.image_set.all()[:4]

    return render_to_response("base.html", dict(albums=albums, user=request.user,
        media_url=MEDIA_URL,images=images))

def about(request):
    return render_to_response('about.html')


def login(request):
    c = {}
    c.update(csrf(request))
    if request.POST:
        username=request.POST.get('username','')
        password=request.POST.get('password','')
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return render_to_response('main.html', auth.get_user(user))
        else:
            c['login_error']="User does not exict"
            return render_to_response('main.html', c)
    else:
        return render_to_response('main.html', c)
def logout(request):
    auth.logout(request)
    return render_to_response('/')

def addComment(request, image_id):
    if request.POST:
        form = CommentForm
        if form.is_valid():
            comment = form.save(commit=False)
            comment.poste_to.get(id=image_id)
            form.save()
    return redirect('/image/%s' % image_id)


def Prewiew(request, image_id):
    args = { }
    img = Image.objects.get(id=image_id)
    args['image'] = Image.objects.get(id=image_id)
    args['album']=img.album.title
    return render_to_response('prewiew.html', args)
def Albums(request):
    args = {}
    alb = Album.objects.get(id=1)
    if alb.public==True:
        #args['images']=
        args['title']= alb.title
        args['likes']=alb.likes
    else:
        redirect("/")
    return render_to_response('album.html', args)