from django.contrib import admin
from . import models

@admin.register(models.UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('username','phone','city')

@admin.register(models.City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('city',)
