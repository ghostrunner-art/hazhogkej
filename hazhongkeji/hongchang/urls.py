# -*- coding: utf-8 -*-

from django.conf.urls import url
from hongchang import views

urlpatterns = [

    url(r'^login$',views.Login.as_view(),name='login'),

    # url(r'^shuju/$',views.Shuju.as_view()),

]