from django.shortcuts import render, HttpResponse
from django.core import serializers
from django.http import JsonResponse
from rest_framework.views import APIView
from . import models


class HazhongSite(APIView):
    def get(self,request,*args,**kwargs):
        context = {}
        s = models.MuluOne.objects.all().first()
        print(s,'**********',type(s))
        context['title'] = s
        # print(context)
        # cc = serializers.serialize('json',context)
        return HttpResponse('hello') #JsonResponse(context,)










# def index(request):
#
#     return render(request, 'index.html')
#
# def about(request):
#
#     return render(request, 'about.html')
#
# def news(request):
#
#     return render(request, 'news.html')
