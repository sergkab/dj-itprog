from django.urls import path
from .views import *

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', home),
    path('test/<myparam>', test),
    path('test/first', first),
    path('readme/', readme),
    path('bogacha/', show_bogacha),
    path('click_butt/', click_butt, ""),
]

