from django.db import models

# Create your models here.

class ShopItem(models.Model):
    item_name = models.CharField(max_length=200)
    item_price = models.FloatField()
    item_desc = models.TextField()
    img_url = models.CharField(max_length=1000, blank=True)
