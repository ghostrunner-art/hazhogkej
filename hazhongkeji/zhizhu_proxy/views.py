from django.views import View
from django.shortcuts import render, HttpResponse
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
            username = form.cleaned_data['username']
            phone_valid = form.cleaned_data['phone']  # 推荐这么取验证后的数据
            # phone = request.POST['phone']  # 取原始数据
            city = form.cleaned_data['choice']
            wb = request.POST['wb']
            if wb == '':
                error_wb = {}
                error_wb['error_wb'] = '网吧不能为空'
                return render(request,'error.html',error_wb)
            wb_name = models.Wangba.objects.filter(id=wb).first()  # 不加.first()是一个可迭代的QuerySet，这里取出第一个值

            centent['phone_valid'] = phone_valid
            centent['city'] = city
            centent['wb'] = wb_name
            centent['username'] = username

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
    def get(self, request):
        reg = request.GET.get('country')
        obj = models.Wangba.objects.filter(wb_for_id=reg)
        # return HttpResponse(obj)
        return render(request, 'city_dropdown_list_options.html', {'objs': obj})
