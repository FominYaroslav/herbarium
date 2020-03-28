from django.db import models

class Plant(models.Model):
    id_of_plant = models.CharField(max_length=15)
    name = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    scan = models.ImageField()


# Create your models here.
