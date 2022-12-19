from django.contrib import admin

# Register your models here.
from .models import Article, Bogacha

admin.site.register(Article)
admin.site.register(Bogacha)

