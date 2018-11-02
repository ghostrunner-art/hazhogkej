from django.views import View
from django.shortcuts import render
from . import models
from .forms import Myforms

class Login(View):
    def get(self, request, *args, **kwargs):
        form = Myforms()
        return render(request, 'login-forms.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = Myforms(request.POST)  # 请求数据做参数
        if form.is_valid():
            centent = {}

            phone_valid = form.cleaned_data['phone']  # 推荐这么取验证后的数据
            phone = request.POST['phone']  # 取原始数据
            centent['phone_valid'] = phone_valid
            centent['phone'] = phone

            print(phone_valid, phone)
            return render(request, 'index.html', centent)
        else:
            error = {}
            error['form'] = form
            error['error'] = form.errors
            return render(request, 'login-forms.html', error)


class zhizhu_index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class Shuju(View):
    def get(self, request, num):
        print(num)
        return render(request, 'error.html')
