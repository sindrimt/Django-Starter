from django.db import models

class Product(models.Model):
    title       = models.CharField(max_length=210) # max length is required for CharField
    description = models.TextField(blank = True, null = True)
    price       = models.DecimalField(decimal_places = 2, max_digits = 10000)
    summary     = models.TextField()
    featured    = models.BooleanField() # null = True, default = True

# Create your models here
