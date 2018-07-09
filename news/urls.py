from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url('^$',views.welcome,name = 'welcome'),
    url('^today/$',views.news_of_day,name='newsToday'),
]
