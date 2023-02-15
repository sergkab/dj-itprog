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

class Category(models.Model):
    name = models.CharField(max_length=30, unique = True, verbose_name = "Название")

class Good(models.Model):
    name = models.CharField(max_length=50, unique = True, verbose_name = "Название")
    description = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null = True, blank = True)
    in_stock = models.BooleanField(default = True, db_index = True)

    def __str__(self):
        s = self.name
        if not self.in_stock:
            s = s + " (нет в наличии)"
        return s

