#encoding: utf8

from django.conf.urls import patterns, include, path
import pro1.app1.views as views

urlpatterns = [
        #top
        path('^$', views.top, name='top'),
]
