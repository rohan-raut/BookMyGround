from typing import Generic
from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from myApp.models import city_name, area_name, sport_name, ground_registration
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . serializers import area_nameSerializer, ground_registrationSerializer, city_nameSerializer, area_nameSerializer, sport_nameSerializer
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
import requests



# Create your views here.

def index(request):
    return render(request, 'index.html')


def loginUser(request):
    if(request.method == "POST"):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, "User not found")
            return redirect('/login')
    else:
        return render(request, 'login.html')


def signupUser(request):
    if(request.method == "POST"):
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if(request.POST.get('is_owner')=='is_owner'):
            is_owner = True
        else:
            is_owner = False

        if(password == confirm_password):
            user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password, is_staff=is_owner)
            user.save()
            messages.success(request, "Registered Successfully! Now you can Log In")
            return redirect('/login')
        else:
            messages.warning(request, "Password doesn't match!")
            return redirect('/sign-up')
    else:
        return render(request, 'signup.html')


def logoutUser(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("/login")


def dashboard(request):
    dic={}
    dic['grounds_registered'] = []
    qset = ground_registration.objects.filter(username = request.user.username)
    for obj in qset:
        dic['grounds_registered'].append(obj)
    dic['grounds_count'] = len(dic['grounds_registered'])
    print(dic['grounds_registered'])
    return render(request, 'my-dashboard.html', dic)


# Ground Registration HTML form page
def ground_registration_func(request):
    if(request.method == "POST"):
        ground_objs = ground_registration.objects.all()
        count=1
        for obj in ground_objs:
            count=count+1
        
        ground_id = "BMG"+ str(count)
        username = request.user.username
        ground_name = request.POST['name_of_ground']
        city = request.POST['city']
        area = request.POST['area']
        owner_name = request.user.first_name +" "+ request.user.last_name
        select_sport = request.POST['select_sport']
        from_time = request.POST['from_time']
        to_time = request.POST['to_time']
        phone = request.POST['phone']
        rates = request.POST['rates']

        ground_registration_obj = ground_registration(ground_id=ground_id, username=username, ground_name=ground_name, city=city, area=area, owner_name=owner_name, sport_name=select_sport, from_time=from_time, to_time=to_time, rates=rates, phone=phone)

        ground_registration_obj.save()

        return redirect('/dashboard')
    else:     
        d={}
        cities = city_name.objects.all()
        areas = area_name.objects.all()
        sports = sport_name.objects.all()
        d['city']=[]
        d['area']=[]
        d['sport']=[]
        for obj in cities:
            d['city'].append(obj.city)

        for x in d['city']:
            d[x]=[]

        for obj in areas:
            d['area'].append(obj.area)
            d[obj.city].append(obj.area)

        for obj in d['area']:
            d[obj]=[]

        for obj in areas:
            d[obj.area].append(obj.city)

        for obj in sports:
            d['sport'].append(obj.sport_ground)

        json_data = json.dumps(d)
        dic={"d": json_data}

        return render(request, 'ground-registration.html', dic)



# Booking the Ground to Play
def booking(request):  
    ground_list_api = "http://127.0.0.1:8000/api/ground-list?"
    if(request.method == "GET"):
        city = request.GET.get('city')
        area = request.GET.get('area')
        sport = request.GET.get('sport')
        if(city!=None and city!="none"):
            ground_list_api = ground_list_api + "city="+city+"&"
        if(area!=None and area!="none"):
            ground_list_api = ground_list_api + "area="+area+"&"
        if(sport!=None and sport!="none"):
            ground_list_api = ground_list_api + "sport_name="+sport+"&"

    response = requests.get(ground_list_api)
    data = response.text
    context = {}
    context['ground_list'] = json.loads(data)
    return render(request, 'booking.html', context)


def ground_detail(request, pk):
    api = "http://127.0.0.1:8000/api/ground-list?ground_id="+pk
    response = requests.get(api)
    data = response.text
    context = {}
    context['ground_detail'] = json.loads(data)[0]
    print(context)
    return render(request, 'ground_detail.html', context)

# See all the booked Grounds by User
def my_bookings(request):
    return render(request, 'my-bookings.html')




# API Data 

class GroundListView(generics.ListAPIView):
    queryset = ground_registration.objects.all()
    serializer_class = ground_registrationSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['city', 'area', 'sport_name', 'ground_id']   

class CityListView(generics.ListAPIView):
    queryset = city_name.objects.all()
    serializer_class = city_nameSerializer

class AreaListView(generics.ListAPIView):
    queryset = area_name.objects.all()
    serializer_class = area_nameSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['city']

class SportsListView(generics.ListAPIView):
    queryset = sport_name.objects.all()
    serializer_class = sport_nameSerializer


# SuperUser:
# username: dbms
# email: dbmsproject@bookmyground
# password: dbms