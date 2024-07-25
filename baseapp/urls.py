from django.contrib import admin
from django.urls import path,include
from baseapp.views import *


urlpatterns = [
    path('', home, name = 'home'),
    path('about', about, name = 'about'),
    path('blogs', blogs, name = 'blog'),
    path('blogs-details', blogsDetails, name = 'blogsDetails'),
    path('services', services, name = 'services'),
    path('portfolio', portfolio, name = 'portfolio'),
    path('contact', contact, name = 'contact'),
]
