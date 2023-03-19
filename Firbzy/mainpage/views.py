from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "mainpage/mainpage.html")

def about(request):
    return render(request, 'mainpage/aboutpage.html')

def item(request):
    return render(request, "mainpage/shoppage.html")

def itemselector1(request):
    return render(request, f"mainpage/item1.html")

def itemselector2(request):
    return render(request, f"mainpage/item2.html")

def itemselector3(request):
    return render(request, f"mainpage/item3.html")

def itemselector4(request):
    return render(request, f"mainpage/item4.html")

def contacts(request):
    return render(request, "mainpage/contact_us.html")