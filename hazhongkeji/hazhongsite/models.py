from django.db import models

class MuluOne(models.Model):
    leibie = models.CharField(max_length=30, verbose_name='类别')
    url = models.CharField(max_length=120, verbose_name='链接')
    title = models.CharField(max_length=240, verbose_name='标题', null=True)
    jianjie = models.TextField(verbose_name='简介', null=True)
    class Meta:
        verbose_name = '主导航'
        verbose_name_plural='主导航'


class MuluTwo(models.Model):
    leibie = models.CharField(max_length=30, verbose_name='类别')
    url = models.CharField(max_length=120, verbose_name='链接')
    title = models.CharField(max_length=240, verbose_name='标题', null=True)
    jianjie = models.TextField(verbose_name='简介', null=True)
    waijian_muluone = models.ForeignKey(to='MuluOne', on_delete=models.CASCADE)
    class Meta:
        verbose_name = '二级导航'
        verbose_name_plural = '二级导航'


class NewsOne(models.Model):
    title = models.CharField(max_length=50, verbose_name='标题')
    timeup = models.DateField(auto_now_add=True,verbose_name='时间')
    textone = models.TextField(verbose_name='正文')
    author = models.CharField(max_length=30,verbose_name='作者')
    waijian_muluone = models.ForeignKey(to='MuluOne',on_delete=models.CASCADE)
    class Meta:
        verbose_name = '主导航对应信息'
        verbose_name_plural = '主导航对应信息'


class NewsTwo(models.Model):
    title = models.CharField(max_length=50, verbose_name='标题')
    timeup = models.DateField(auto_now_add=True, verbose_name='时间')
    textone = models.TextField(verbose_name='正文')
    author = models.CharField(max_length=30, verbose_name='作者')
    waijian_mulutwo = models.ForeignKey(to='MuluTwo', on_delete=models.CASCADE)
    class Meta:
        verbose_name = '二级导航对应信息'
        verbose_name_plural = '二级导航对应信息'

class Otherone(models.Model):
    title = models.CharField(max_length=500,verbose_name='预留字段(charm)')
    textone = models.TextField(verbose_name='预留字段(Text)')

    class Meta:
        verbose_name = '其他表'
        verbose_name_plural = '其他表'

