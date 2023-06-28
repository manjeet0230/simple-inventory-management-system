from django.db import models

class Product(models.Model):
    Name=models.CharField(max_length=50, null=False)
    Description=models.TextField()
    Quantity=models.IntegerField()
    Price=models.DecimalField(max_digits=5, decimal_places=2)

# Create your models here.
