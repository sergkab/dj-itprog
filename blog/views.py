from django.shortcuts import render
from django.http import HttpResponse
from .models import Article, Bogacha
from django.conf import settings

# Create your views here.
def home(request):
    posts = Article.objects.all()
    return render( request, 'blog/home.html', { 'posts': posts } )

def test(request, myparam ):
    #return HttpResponse('<h2> Hello! I am Test 2022 11 06 </h2> <p> <h2> Test Page 05 after Amend  </h2> </p> ')
    statdirs = settings.STATICFILES_DIRS
    staturl = settings.STATIC_URL
    basdir = settings.BASE_DIR
    statroot = settings.STATIC_ROOT
    context = { 'statdirs': statdirs, 'staturl': staturl, 'basdir': basdir, 'statroot': statroot, 'myparam': myparam }
    return render( request, 'blog/test.html', context )

def first(request):
    #return HttpResponse('<h2> Hello! I am Test/first 2022 11 22 </h2> <p> <h2> Test Page 06   </h2> </p> ')
    return render( request, 'blog/first.html' )

def readme(request):
    return render( request, 'blog/readme.html' )





