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


class ground_registration(models.Model):
    ground_id = models.CharField(max_length=10, primary_key=True)
    username = models.CharField(max_length=50)
    ground_name = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    area = models.CharField(max_length=50)
    owner_name = models.CharField(max_length=100)
    sport_name = models.CharField(max_length=50)
    from_time = models.TimeField()
    to_time = models.TimeField()
    rates = models.IntegerField()
    phone = models.IntegerField()
    ground_image = models.ImageField(upload_to="myApp/ground_images", default="")


class booking(models.Model):
    booking_id = models.CharField(max_length=10, primary_key=True)
    username = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    area = models.CharField(max_length=50)
    sport = models.CharField(max_length=50)
    sport_complex = models.CharField(max_length=100)
    date = models.DateField()
    from_time = models.TimeField()
    to_time = models.TimeField()