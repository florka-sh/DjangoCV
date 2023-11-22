# cv_app/urls.py

from django.urls import path
from .views import cv

urlpatterns = [
    path('', cv, name='cv'),
]
