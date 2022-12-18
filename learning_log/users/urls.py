"""Defines URL patterns for users"""
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
from . import views



urlpatterns = [
    # Login page
    url(r'^login/$', LoginView.as_view(),{'registration/login.html': 'users/login.html'}, name='login'),
    # Logout page
    url(r'^logout/$', views.logout_view, name='logout'),
    # Registration page
    url(r'^register/$', views.register, name='register'), 
]