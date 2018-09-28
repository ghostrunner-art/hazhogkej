# -*- coding: utf-8 -*-

from django.conf.urls import url
from hazhongsite import views

urlpatterns = [
    url(r'^$',views.HazhongSite.as_view()),
    # url(r'^$', views.index),
    # url(r'^index', views.index),
    # url(r'^about', views.about),
    # url(r'^', views.index),
    # url(r'^', views.index),
    # url(r'^', views.index),
]