from django.db import models


class UserInfo(models.Model):
    username = models.CharField(max_length=32, verbose_name='用户名')
    pwd = models.CharField(max_length=32)

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username

