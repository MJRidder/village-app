"""
URL configuration for village_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('support/', include('support.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', include(
        'about.urls'), name='about-urls'),
    path('faq/', include(
        'faq.urls'), name='faq-urls'),
    path('contact/', include(
        'contact.urls'), name='support-urls'),
    path('', include(
        'support.urls'), name='support-urls'),
    path('accounts/', include(
        'allauth.urls')),
    path('summernote/', include(
        'django_summernote.urls')),
]
