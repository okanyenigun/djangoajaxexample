from curses.ascii import HT
from django.http import HttpRequest
from django.shortcuts import render
from django.http.request import HttpRequest
from django.views.generic import View
from django.http import JsonResponse
# Create your views here.

class Viewer(View):

    def get(self,request:HttpRequest):
        if request.GET.get('val'):
            value = float(request.GET.get('val'))
            value += 10
            print("value: ",value)
            return JsonResponse({'data':value},status=200)
        return render(request,'./templates/index.html')

    def post(self,request:HttpRequest):
        return render(request,'./templates/index.html')


