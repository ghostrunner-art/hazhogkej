# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

from django.conf.urls import url
from xinhongguang import views

urlpatterns = [
    url(r'^$', views.XinSite.as_view()),
]
