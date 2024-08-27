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
    
    # Basic Pages
    path('shipping-policy', shipping, name='shipping_policy'),
    path('refund-policy', refund, name='refund_policy'),
    path('privacy-policy', privacy_policy, name='privacy_policy'),
    path('terms-and-conditions', termsconditions, name='termsconditions'),
]
