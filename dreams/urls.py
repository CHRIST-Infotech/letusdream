from django.contrib import admin
from django.urls import path, include

from main.views import index

urlpatterns = [
    path('', index, name='main'),
]
