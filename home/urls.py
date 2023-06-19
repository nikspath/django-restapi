from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('all_post/',all_post,name="all_post"),
    path("send_email_user/",send_email_user,name="send_email_user"),
]