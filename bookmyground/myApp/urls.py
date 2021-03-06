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
    path("booking", views.booking_func, name="booking"),
    path("booking/<str:pk>", views.ground_detail, name="ground_detail"),
    path("my-bookings", views.my_bookings, name="my-bookings"),
    path('api/ground-list', views.GroundListView.as_view()),
    path('api/cities', views.CityListView.as_view()),
    path('api/areas', views.AreaListView.as_view()),
    path('api/sports', views.SportsListView.as_view()),
    path('api/booking', views.BookingListView.as_view()),
    # path("sign", views.sign, name="sign"),
    path("profile", views.profile, name="profile"),
    path("history", views.history, name="history")

]