from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.TextField(default='producto name')
    description = models.TextField(default='this is the description')
    price = models.TextField(default='200')
    summary = models.TextField(default='this is cool!')