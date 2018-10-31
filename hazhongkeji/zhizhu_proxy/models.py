from django.db import models



class UserInfo(models.Model):

    username = models.CharField(max_length=32, verbose_name='姓名')
    phone = models.CharField(max_length=32, verbose_name='联系方式', unique=True)
    number = models.CharField(max_length=32, verbose_name='网吧代码')
    city = models.CharField(choices=None,max_length=32, null=True, verbose_name='城区')
    wb = models.CharField(max_length=32, null=True, verbose_name='网吧')

    class Meta:
        verbose_name = '报名信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username

class City(models.Model):
    city = models.CharField(max_length=32, verbose_name='城区')

    class Meta:
        verbose_name = '城区名称'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.city


class Wangba(models.Model):
    wb = models.CharField(max_length=32,verbose_name='网吧名称',null=True)
    wb_for = models.ForeignKey(to=City, max_length=32, verbose_name='属于哪个区',null=True)

    class Meta:
        verbose_name = '网吧名称'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.wb
