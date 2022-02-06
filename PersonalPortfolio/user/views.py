from django import views
from django.shortcuts import render
from django.views import View

# Create your views here.

class Home(views.View):
    def get(self,request):
        return render(request,'index.html')
