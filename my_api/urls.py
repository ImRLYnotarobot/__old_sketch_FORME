from django.urls import path

from . import views


urlpatterns = [
    path('coef_from_rur/', views.main),
]
