from django.contrib import admin

# Register your models here.
from .models import Article, Bogacha, Boga_Mesto

admin.site.register(Article)
admin.site.register(Bogacha)
admin.site.register(Boga_Mesto)


