from django.conf.urls import patterns, include, url
from django.contrib import admin
import views

urlpatterns = patterns('',
   

    url(r'^add/?', views.addData ),
)