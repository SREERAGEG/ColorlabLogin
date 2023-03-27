from django.shortcuts import render
from django.http import HttpResponse
from . models import UserData
# Create your views here.
def index(request):
    user= UserData.objects.all()
    return render(request,'index.html')
    #return HttpResponse("<h1>Hello</h1>")