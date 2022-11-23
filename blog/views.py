from django.shortcuts import render
from django.http import HttpResponse
from .models import Article

# Create your views here.
def home(request):
    posts = Article.objects.all()
    return render( request, 'blog/home.html', { 'posts': posts } )

def test(request):
    return HttpResponse('<h2> Hello! I am Test 2022 11 06 </h2> <p> <h2> Test Page 05 after Amend  </h2> </p> ')

def first(request):
    return HttpResponse('<h2> Hello! I am Test/first 2022 11 22 </h2> <p> <h2> Test Page 06   </h2> </p> ')


