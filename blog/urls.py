from django.urls import path
from .views import *

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', home),
    path('test/<myparam>', test),
    path('test/first', first),
    path('readme/', readme),
    path('bogacha/', show_bogacha),
    path('click_butt/<myparam>', click_butt, ""),
    path('show_mesto/<myparam>', show_mesto, ""),
    path('before_show_mesto/<myparam>', before_show_mesto, ""),
    path('index_good/', index_good),
]

