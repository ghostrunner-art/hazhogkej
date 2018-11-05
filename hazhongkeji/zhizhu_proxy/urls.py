# -*- coding: utf-8 -*-

from django.conf.urls import url
from zhizhu_proxy import views

urlpatterns = [
    url(r'^index$',views.zhizhu_index.as_view(),name='index'),
    url(r'^login$',views.Login.as_view()),
    # url(r'^login$',views.login),
    # url(r'^shuju/page(?P<num>[0-9]+)/$',views.Shuju.as_view()),
    url(r'^shuju/$',views.Shuju.as_view()),

]