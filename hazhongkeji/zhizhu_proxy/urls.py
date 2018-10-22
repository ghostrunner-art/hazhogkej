# -*- coding: utf-8 -*-

from django.conf.urls import url
from zhizhu_proxy import views

urlpatterns = [
    url(r'^index$',views.zhizhu_index.as_view()),
    url(r'^login$',views.Login.as_view()),

]