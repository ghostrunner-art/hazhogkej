# -*- coding: utf-8 -*-


from django.conf.urls import url
from xiaohua_spider import views

urlpatterns = [
    url(r'^index$',views.Xiaohua_index.as_view(),name='index'),

]