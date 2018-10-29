from django.contrib import admin
from . import models

@admin.register(models.UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('username','phone','number')

