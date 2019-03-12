# -*- coding: utf-8 -*-
from django.conf.urls import url
from myauth import views

urlpatterns = [
    url(r'^weixin$',views.WeixinAuth.as_view(),name='weixinauth'),
]
