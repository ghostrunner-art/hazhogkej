from django.views import View
from django.shortcuts import render
from . import models


class Login(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'login.html')

    def post(self, request):
        centent = {}
        phone = request.POST['phone']
        username = request.POST['username']
        number = request.POST['number']
        models.UserInfo.objects.create(username=username, phone=phone, number=number)

        centent['username'] = username
        centent['phone'] = phone
        centent['number'] = number
        print('ok')
        return render(request, 'index.html', centent)


class zhizhu_index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')
