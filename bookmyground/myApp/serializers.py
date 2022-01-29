from attr import fields
from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from .models import ground_registration, city_name, area_name, sport_name


# Serializers define the API representation.

class ground_registrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ground_registration
        fields = "__all__"


class city_nameSerializer(serializers.ModelSerializer):
    class Meta:
        model = city_name
        fields = "__all__"


class area_nameSerializer(serializers.ModelSerializer):
    class Meta:
        model = area_name
        fields = "__all__"

class sport_nameSerializer(serializers.ModelSerializer):
    class Meta:
        model = sport_name
        fields = "__all__"
