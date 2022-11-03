from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('<h2> Hello! I fm Django 2022 11 03 </h2> <p> <h2> once more 02  </h2> </p> ')

def test(request):
    return HttpResponse('<h2> Hello! I fm Test 2022 11 03 </h2> <p> <h2> Test Page 03  </h2> </p> ')


