from django.db import models


# Create your models here.
class Product(models.Model):
    prodNm = models.CharField(max_length=30)
    stckQty = models.IntegerField()
    brnd = models.CharField(max_length=6)
    cate = models.CharField(max_length=3)