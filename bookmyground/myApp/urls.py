from django.contrib import admin
from django.urls import path
from myApp import views

urlpatterns = [
    path("", views.index, name='home'),
    path("login", views.loginUser, name='login'),
    path("sign-up", views.signupUser, name='sign-up'),
    path("logout", views.logoutUser, name='logout'),
    path("dashboard", views.dashboard, name="dashboard"),
    path("ground-registration", views.ground_registration_func, name="ground-registration"),
    path("booking", views.booking, name="booking"),
    path("my-bookings", views.my_bookings, name="my-bookings")

]