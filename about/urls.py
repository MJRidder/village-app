from . import views
from django.urls import path

urlpatterns = [
    path('', views.about_village, name='about'),
]