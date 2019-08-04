from django.shortcuts import render
from django.http import HttpResponse


def click_on_car(request):
    return render(request, 'click_on_car.html')
