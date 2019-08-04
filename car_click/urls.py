from django.urls import path
from . import views

urlpatterns = [
    path('', views.click_on_car, name='car_url'),
]
