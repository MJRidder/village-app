from . import views
from django.urls import path

urlpatterns = [
    path('', views.SupportList.as_view(), name='home'),
]
