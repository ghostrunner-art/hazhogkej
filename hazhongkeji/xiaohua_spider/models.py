from django.db import models


# Create your models here.
class Xiaohua(models.Model):
    x_id = models.IntegerField(unique=True, null=True)
    x_title = models.CharField(max_length=256, verbose_name='笑话标题')
    x_create_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')
    x_source = models.CharField(max_length=128, null=True, verbose_name='爬取来源')
    x_img_url = models.TextField(verbose_name='图片链接')
    x_tags = models.ManyToManyField('Tags', verbose_name='标签集合', blank=True)
    x_text = models.TextField(null=True, verbose_name='笑话内容')
    x_img = models.ImageField(null=True, verbose_name='笑话图片')
    x_html_text = models.TextField(null=True, verbose_name='html文本')

    class Meta:
        verbose_name = '笑话信息'
        verbose_name_plural = verbose_name



    def __str__(self):
        return self.x_title


class Tags(models.Model):
    tags_name = models.CharField(max_length=128, verbose_name='标签名字', null=True)
    tags_create_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name


    def __str__(self):
        return self.tags_name
