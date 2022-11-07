from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('<h2> Hello! I fm Django 2022 11 06 </h2> <p> <h2> once more 03  </h2> </p> ')

def test(request):
    return HttpResponse('<h2> Hello! I am Test 2022 11 06 </h2> <p> <h2> Test Page 05 after Amend  </h2> </p> ')


