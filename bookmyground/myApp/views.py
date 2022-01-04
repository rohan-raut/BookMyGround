from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from myApp.models import city_name, area_name, sport_name
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
    return render(request, 'my-dashboard.html')


def ground_registration(request):
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


# SuperUser:
# username: dbms
# email: dbmsproject@bookmyground
# password: dbms