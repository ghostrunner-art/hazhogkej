from django.views import View
from django.shortcuts import render
from django.db import IntegrityError
from . import models
from .forms import Myforms


class Login(View):
    def get(self, request):
        form = Myforms()
        return render(request, 'login-forms.html', {'form': form})

    def post(self, request):
        form = Myforms(request.POST)  # 请求数据做参数
        if form.is_valid():
            centent = {}
            username = form.cleaned_data['username']
            phone_valid = form.cleaned_data['phone']  # 推荐这么取验证后的数据
            # phone = request.POST['phone']  # 取原始数据
            city = form.cleaned_data['choice']
            try:
                wb = request.POST['wb']
                wb_name = models.Wangba.objects.filter(id=wb).first()  # 不加.first()是一个可迭代的QuerySet，这里取出第一个值
            except:
                return render(request, 'error.html', )
            centent['phone_valid'] = phone_valid
            centent['city'] = city
            centent['wb'] = wb_name
            centent['username'] = username
            try:
                models.UserInfo.objects.create(username=username, phone=phone_valid, city=city, wb=wb_name)
            except IntegrityError:
                return render(request, 'error2.html', )

            return render(request, 'index.html', centent)
        else:
            error = {}
            error['form'] = form
            error['error'] = form.errors
            return render(request, 'error.html', error)


class zhizhu_index(View):
    def get(self, request):
        return render(request, 'login.html')


class Shuju(View):
    def get(self, request):
        reg = request.GET.get('country')
        obj = models.Wangba.objects.filter(wb_for_id=reg)
        return render(request, 'city_dropdown_list_options.html', {'objs': obj})
