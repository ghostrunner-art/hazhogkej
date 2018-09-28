from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView

from rest_framework.authentication import BaseAuthentication


class MyAuth(BaseAuthentication):
    def authenticator(self,request):
        pass



class HazhongSite(APIView):
    authentication_classes = [MyAuth,]

    def get(self):
        self.dispatch
        pass
    
# def index(request):
#
#     return render(request, 'index.html')
#
# def about(request):
#
#     return render(request, 'about.html')
#
# def news(request):
#
#     return render(request, 'news.html')
