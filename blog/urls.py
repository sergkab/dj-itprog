from django.urls import path
from .views import *

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', home),
    path('test/<myparam>', test),
    path('test/first', first),
    path('readme/', readme),
    path('show_bogacha/', show_bogacha),
]

