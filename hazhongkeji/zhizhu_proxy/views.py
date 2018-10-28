import json
from django.views import View

from django.shortcuts import redirect
from django.http import HttpResponse
from django.shortcuts import render
from . import models


class Login(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'login.html')

    def post(self, request, *args, **kwargs):
        print('ok')
        return render(request, 'index.html')


class zhizhu_index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')

from django.db import transaction