from django.contrib import admin
from . import models

@admin.register(models.Xiaohua)
class XiaohuaAdmin(admin.ModelAdmin):
    list_display = ('x_id','x_title','x_source')

@admin.register(models.Tags)
class Tags(admin.ModelAdmin):
    list_display = ('tags_name','tags_create_time',)