# -*- coding: utf-8 -*-
from django import forms
from . import models


class Myforms(forms.Form):
    cc = models.City.objects.all()
    username = forms.CharField(
        label='姓名',
        max_length=32,
        error_messages={
            'required': '姓名不能为空',
            'invalid': '格式错误',
        },
    )
    phone = forms.CharField(
        label='联系方式',
        max_length=11,
        min_length=11,
        error_messages={
            'required': '电话号不能为空',
            'invalid': '格式错误',
            'max_length': '电话号必须为11位',
            'min_length': '电话号必须为11位',
        },
    )
    # number = forms.CharField(label='网吧代码',max_length=32)
    choice = forms.ModelChoiceField(
        label='地区选择',
        queryset=cc,
        empty_label='选择地区',
        error_messages={
            'required': '地区为必选项',
            'invalid': '格式错误',
        },
    )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['choice'].queryset = models.City.objects.all()







