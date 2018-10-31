# -*- coding: utf-8 -*-
from django import forms
from . import models


class Myforms(forms.Form):
    cc = models.City.objects.all()
    username = forms.CharField(label='姓名',max_length=32)
    phone = forms.CharField(
        label='联系方式',
        max_length=11,
        min_length=11,
    )
    number = forms.CharField(label='网吧代码',max_length=32)
    choice = forms.ModelChoiceField(label='地区选择',queryset=cc,empty_label='选择地区',)


