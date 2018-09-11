from django.db import models


class MuluOne(models.Model):
    leibie = models.CharField(max_length=30, verbose_name='类别')
    lianjie = models.CharField(max_length=120, verbose_name='链接')
    title = models.CharField(max_length=240, verbose_name='标题', null=True)
    jianjie = models.TextField(verbose_name='标题', null=True)


class MuluTwo(models.Model):
    leibie = models.CharField(max_length=30, verbose_name='类别')
    lianjie = models.CharField(max_length=120, verbose_name='链接')
    title = models.CharField(max_length=240, verbose_name='标题', null=True)
    jianjie = models.TextField(verbose_name='标题', null=True)
    wijian_one = models.ForeignKey(to='MuluOne',on_delete=models.CASCADE)

