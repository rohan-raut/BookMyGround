from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from myApp.models import city_name, area_name, sport_name, ground_registration
import json



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
    dic={}
    cities = city_name.objects.all()
    areas = area_name.objects.all()
    sports = sport_name.objects.all()
    sports_complex = ground_registration.objects.all()
    dic['cities'] = []
    dic['areas'] = []
    dic['sports'] = []
    dic['sports_complex'] = []

    for city in cities:
        dic['cities'].append(city.city)
    
    for area in areas:
        dic['areas'].append(area.area)
    
    for sport in sports:
        dic['sports'].append(sport.sport_ground)
        dic[sport.sport_ground] = []

    # for complex in sports_complex:
    #     if complex.ground_name not in dic['sports_complex']:
    #         dic['sports_complex'].append(complex.ground_name)
    #     dic[complex] = []

    for sport in dic['sports']:
        sports_name = ground_registration.objects.filter(sport_name=sport)
        for sport_obj in sports_name:
            dic[sport].append(sport_obj.ground_name)

    for grounds_name in dic['sports_complex']:
        sports_ground = ground_registration.objects.filter(ground_name = grounds_name)
        for sport_ground in sports_ground:
            dic[sport_ground.ground_name].append(sport_ground.sport_name)

    for city in dic['cities']:
        dic[city]={}
        dic[city]['areas'] = []
        areas_in_city = area_name.objects.filter(city=city)
        for area in areas_in_city:
            dic[city]['areas'].append(area.area)
            dic[city][area.area] = {}
            dic[city][area.area]['sports'] = []
            dic[city][area.area]['sports_complex'] = []
        sports_in_city = ground_registration.objects.filter(city=city)
        dic[city]['sports'] = []
        for sport in sports_in_city:
            if sport.sport_name not in dic[city]['sports']:
                dic[city]['sports'].append(sport.sport_name)
        sport_complex = ground_registration.objects.filter(city=city)        
        dic[city]['sports_complex'] = []
        for complex in sport_complex:
            if complex.ground_name not in dic[city]['sports_complex']:
                dic[city]['sports_complex'].append(complex.ground_name)
        for complex_name in dic[city]['sports_complex']:
            dic[city][complex_name] = []
        for sport in dic[city]['sports']:
            dic[city][sport]=[]
            sports_for_complex = ground_registration.objects.filter(city=city, sport_name=sport)
            for sport_for_complex in sports_for_complex:
                dic[city][sport].append(sport_for_complex.ground_name)
                dic[city][sport_for_complex.ground_name].append(sport)

        for city_area in dic[city]['areas']:
            sports_with_complex = ground_registration.objects.filter(city=city, area=city_area)
            for sport_with_complex in sports_with_complex:
                dic[city][city_area]['sports'].append(sport_with_complex.sport_name)
                if sport_with_complex not in dic[city][city_area]['sports_complex']:
                    dic[city][city_area]['sports_complex'].append(sport_with_complex.ground_name)



#########################################################
        # for area in dic['areas']:
        #     dic[city][area] = {}
        #     sport_in_area = ground_registration.objects.filter(area=area)
        #     dic[city][area]['sports'] = []
        #     for sport in sport_in_area:
        #         if sport.sport_name not in dic[city][area]['sports']:
        #             dic[city][area]['sports'].append(sport.sport_name)
        #     sport_complex = ground_registration.objects.filter(area=area)
        #     dic[city][area]['sports_complex'] = []
        #     for complex in sport_complex:
        #         if complex.ground_name not in dic[city][area]['sports_complex']:
        #             dic[city][area]['sports_complex'].append(complex.ground_name)
    
    print(dic)
    
    return render(request, 'booking.html')


# See all the booked Grounds by User
def my_bookings(request):
    return render(request, 'my-bookings.html')




# SuperUser:
# username: dbms
# email: dbmsproject@bookmyground
# password: dbms