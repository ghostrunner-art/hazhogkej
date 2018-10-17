import json
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework import serializers
from . import models


class MuluOneSerializers(serializers.ModelSerializer):


    class Meta:
        model = models.MuluOne
        fields = ['id','leibie', 'url', 'title', 'jianjie','image_MuluOne']
        depth = 2

class HazhongSite(APIView):
    parser_classes = [JSONParser, ]

    def get(self, request, *args, **kwargs):
        obj = models.MuluOne.objects.all().order_by('title')
        ser = MuluOneSerializers(instance=obj, many=True)
        return JsonResponse(ser.data,safe=False)
