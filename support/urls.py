from django.contrib import admin
from . import views
from django.urls import path

# QUESTION : is the 'admin' path needed here? As is the import admin?
urlpatterns = [
    path('', views.SupportList.as_view(), name='home'),
    # path('admin/', admin.site.urls),
    path('<slug:slug>/', views.support_detail, name='support_detail'),

]
