from django.db import models

# Create your models here.

class city_name(models.Model):
    city = models.CharField(max_length=50, primary_key = True)

class area_name(models.Model):
    class Meta:
        unique_together = [['area', 'city']]
    area = models.CharField(max_length=50)
    city = models.CharField(max_length=50)

class sport_name(models.Model):
    sport_ground = models.CharField(max_length=100, primary_key=True)