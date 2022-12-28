from django.shortcuts import render
from django.http import HttpResponse
from .models import Article, Bogacha, Boga_Mesto
from django.conf import settings

var_test = "vartest"

# Create your views here.
def home(request):
    posts = Article.objects.all()
    global var_test
    var_test = "vartest_chg_in_home"
    return render( request, 'blog/home.html', { 'posts': posts, 'var_test': var_test } )


def test(request, myparam ):
    #return HttpResponse('<h2> Hello! I am Test 2022 11 06 </h2> <p> <h2> Test Page 05 after Amend  </h2> </p> ')
    statdirs = settings.STATICFILES_DIRS
    staturl = settings.STATIC_URL
    basdir = settings.BASE_DIR
    statroot = settings.STATIC_ROOT
    #var_test = "vartest_chg_in_test"
    context = { 'statdirs': statdirs, 'staturl': staturl, 'basdir': basdir, 'statroot': statroot, 'myparam': myparam, 'var_test': var_test}
    return render( request, 'blog/test.html', context )

def first(request):
    #return HttpResponse('<h2> Hello! I am Test/first 2022 11 22 </h2> <p> <h2> Test Page 06   </h2> </p> ')
    return render( request, 'blog/first.html' )

def readme(request):
    return render( request, 'blog/readme.html' )

def show_bogacha(request):
    posts = Bogacha.objects.all()
    postsm = Boga_Mesto.objects.all()
    global var_test
    var_test = " vartest_chg_in_show_bog "
    return render( request, 'blog/show_bogacha.html', { 'posts': posts, 'postsm': postsm, 'var_test': var_test } )

def click_butt(request, myparam):
    print ("click_button", myparam)
    return HttpResponse( "Hello!" )


