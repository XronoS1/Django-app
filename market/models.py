from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category (models.Model):
    name = models.CharField(max_length=50)


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    rate = models.IntegerField(default=0)
    count = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    photo = models.ImageField(blank=True, null=True)

    category = models.ForeignKey(Category, on_delete=models.PROTECT)


class Comments(models.Model):
    comment = models.TextField()

    user = models.ForeignKey(User, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)


class Delivery(models.Model):
    finished = models.BooleanField(default=False)

    user = models.OneToOneField(User, on_delete=models.PROTECT)
    product = models.OneToOneField(Product, on_delete=models.PROTECT)


#  ToDo: обновление рейтинга товара после добавления комментария
