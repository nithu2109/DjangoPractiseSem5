from django.db import models

ch = [("oil", "oil"), ("grains", "grains"), ("cosmetics", "cosmetics")]
# Create your models here.
class Grocery(models.Model):
    name=models.CharField(max_length=100)
    type=models.CharField(max_length=100,choices=ch, default="oil")
    quantity=models.IntegerField()
    rate_per_unit = models.IntegerField()
    amount = models.IntegerField(default=0)
