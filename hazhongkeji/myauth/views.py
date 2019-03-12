from django.shortcuts import render
from django import views
from django.http import HttpResponse

# Create your views here.

class WeixinAuth(views.View):
    def get(self,request):
        return HttpResponse('ok')


