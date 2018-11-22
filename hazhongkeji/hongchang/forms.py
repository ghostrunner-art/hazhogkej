# -*- coding: utf-8 -*-
from django import forms
from . import models


class Mytoforms(forms.Form):
    cc = models.City.objects.all()
    username = forms.CharField(
        max_length=32,
        error_messages={
            'required': '姓名不能为空',
            'invalid': '格式错误',
        },
    )

    phone = forms.CharField(
        max_length=11,
        min_length=11,
        error_messages={
            'required': '电话号不能为空',
            'invalid': '格式错误',
            'max_length': '电话需为11位数字',
            'min_length': '电话需为11位数字',

        },
    )
    # number = forms.CharField(label='网吧代码',max_length=32)
    choice = forms.ModelChoiceField(

        queryset=cc,
        empty_label='选择地区',
        error_messages={
            'required': '地区为必选项',
            'invalid': '格式错误',
        },
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['choice'].queryset = models.City.objects.all()
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

