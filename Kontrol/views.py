from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request,"blog/login.html")

def main(request):
    return render(request,"blog/index.html")