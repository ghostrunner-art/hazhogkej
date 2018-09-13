from django.contrib import admin
from .models import MuluTwo, MuluOne, NewsOne, NewsTwo, Otherone

@admin.register(MuluOne)
class MuluOneAdmin(admin.ModelAdmin):
    list_display = ('leibie','url','title','jianjie')


class MuluTwoAdmin(admin.ModelAdmin):
    pass


class NewsOneAdmin(admin.ModelAdmin):
    pass


class NewsTwoAdmin(admin.ModelAdmin):
    pass


class OtheroneAdmin(admin.ModelAdmin):
    pass


# admin.site.register(MuluOne, MuluOneAdmin)
admin.site.register(MuluTwo)
admin.site.register(NewsOne)
admin.site.register(NewsTwo)
admin.site.register(Otherone)
