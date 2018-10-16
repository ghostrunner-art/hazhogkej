# -*- coding: utf-8 -*-

from django.conf.urls import url
from hazhongsite import views

urlpatterns = [
    url(r'^$',views.HazhongSite.as_view()),
]