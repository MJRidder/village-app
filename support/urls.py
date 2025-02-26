from . import views
from django.urls import path


urlpatterns = [
    path('', views.SupportList.as_view(), name='home'),
    path('<slug:slug>/', views.support_detail, name='support_detail'),
    path('<slug:slug>/edit_reply/<int:reply_id>',
         views.reply_edit, name='reply_edit'),

]
