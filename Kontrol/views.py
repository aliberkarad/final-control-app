from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request,"blog/login.html")

def ayaz(request):
    return render(request,"blog/ayaz.html")