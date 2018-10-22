import json
from django.views import View
from django.http import HttpResponse
from django.shortcuts import render
from . import models


class Login(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'login.html')


class zhizhu_index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')
