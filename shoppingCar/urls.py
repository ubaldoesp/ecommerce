from django.contrib import admin
from django.conf.urls import url
from django.urls import path,include
from shoppingCar.views import *

urlpatterns = [
    path('cart', CartView.as_view())
]
