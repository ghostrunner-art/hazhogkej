from django.contrib import admin
from .models import MuluTwo, MuluOne, NewsOne, NewsTwo, Otherone

@admin.register(MuluOne)
class MuluOneAdmin(admin.ModelAdmin):
    list_display = ('leibie','url','title','jianjie')
@admin.register(MuluTwo)
class MuluTwoAdmin(admin.ModelAdmin):
    list_display = ('leibie', 'url', 'title', 'jianjie')
@admin.register(NewsOne)
class NewsOneAdmin(admin.ModelAdmin):
    list_display = ('title', 'timeup', 'textone', 'author')
@admin.register(NewsTwo)
class NewsTwoAdmin(admin.ModelAdmin):
    list_display = ('title', 'timeup', 'textone', 'author')
@admin.register(Otherone)
class OtheroneAdmin(admin.ModelAdmin):
    list_display = ('title', 'textone')

