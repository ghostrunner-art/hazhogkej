from django.contrib import admin
from . import models

@admin.register(models.UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('username','phone','number')

@admin.register(models.City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('city',)

@admin.register(models.Wangba)
class CityAdmin(admin.ModelAdmin):
    list_display = ('wb','wb_for')