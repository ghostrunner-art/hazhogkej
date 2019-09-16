from django.db import models
from mdeditor.fields import MDTextField

class MuluOne(models.Model):
    leibie = models.CharField(max_length=30, verbose_name='类别')
    url = models.CharField(max_length=120, verbose_name='链接')
    title = models.CharField(max_length=240, verbose_name='标题', null=True)
    jianjie = models.TextField(verbose_name='简介', null=True)
    image_MuluOne = models.ImageField(upload_to='./mdeia/images',null=True)

    class Meta:
        verbose_name = '主导航'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.leibie

class MuluTwo(models.Model):
    waijian_muluone = models.ForeignKey(to='MuluOne', on_delete=models.CASCADE, verbose_name='关联一级目录')
    leibie = models.CharField(max_length=30, verbose_name='类别')
    url = models.CharField(max_length=120, verbose_name='链接')
    title = models.CharField(max_length=240, verbose_name='标题', null=True)
    jianjie = models.TextField(verbose_name='简介', null=True)

    class Meta:
        verbose_name = '二级导航'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.leibie

class NewsOne(models.Model):
    waijian_muluone = models.ForeignKey(to='MuluOne', on_delete=models.CASCADE, verbose_name='关联目录')
    title = models.CharField(max_length=50, verbose_name='标题')
    timeup = models.DateField(auto_now_add=True, verbose_name='时间')
    textone = MDTextField(verbose_name='正文')
    author = models.CharField(max_length=30, verbose_name='作者')

    class Meta:
        verbose_name = '主导航信息列表'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.title

class NewsTwo(models.Model):
    waijian_mulutwo = models.ForeignKey(to='MuluTwo', on_delete=models.CASCADE, verbose_name='关联目录')
    title = models.CharField(max_length=50, verbose_name='标题')
    timeup = models.DateField(auto_now_add=True, verbose_name='时间')
    textone = MDTextField(verbose_name='正文')
    author = models.CharField(max_length=30, verbose_name='作者')


    class Meta:
        verbose_name = '二级导航信息列表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

class Otherone(models.Model):
    title = models.CharField(max_length=500, verbose_name='预留字段(charm)')
    textone = models.TextField(verbose_name='预留字段(Text)')

    class Meta:
        verbose_name = '其他表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
