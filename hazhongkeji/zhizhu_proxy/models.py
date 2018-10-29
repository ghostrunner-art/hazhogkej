from django.db import models


class UserInfo(models.Model):
    username = models.CharField(max_length=32, verbose_name='姓名')
    phone = models.CharField(max_length=32,verbose_name='联系方式')
    number = models.CharField(max_length=32,verbose_name='网吧代码')

    class Meta:
        verbose_name = '报名信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username

