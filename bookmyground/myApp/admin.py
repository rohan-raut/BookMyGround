from django.contrib import admin
from myApp.models import city_name, area_name, sport_name, ground_registration, booking

# Register your models here.
admin.site.register(city_name)
admin.site.register(area_name)
admin.site.register(sport_name)
admin.site.register(ground_registration)
admin.site.register(booking)