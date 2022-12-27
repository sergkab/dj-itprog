from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length = 255)
    content = models.TextField(blank = True)
    created_at = models.DateTimeField(auto_now_add = True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')

class Bogacha(models.Model):
    name = models.CharField(max_length = 80)
    mesto1 = models.CharField(max_length = 80)
    mesto2 = models.CharField(max_length = 80)
    #photo = models.ImageField(upload_to='photos/%Y/%m/%d')

class Boga_Mesto(models.Model):
    mesto1 = models.CharField(max_length = 80)
    mesto2 = models.CharField(max_length = 80)


