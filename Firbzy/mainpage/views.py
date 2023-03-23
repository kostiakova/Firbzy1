from django.http import HttpResponse
from django.shortcuts import render
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    with open("/home/kostinus/PycharmProjects/Firbzy1/Firbzy/mainpage/log_ip.txt", "a") as logs:
        logs.writelines(f"ip == {ip}, name == \n")
        logs.close()
    print(ip)
# Create your views here.
def index(request):
    get_client_ip(request)
    return render(request, "mainpage/mainpage.html")

def about(request):
    get_client_ip(request)
    return render(request, 'mainpage/aboutpage.html')

def item(request):
    get_client_ip(request)
    return render(request, "mainpage/shoppage.html")

def itemselector1(request):
    get_client_ip(request)
    return render(request, f"mainpage/item1.html")

def itemselector2(request):
    get_client_ip(request)
    return render(request, f"mainpage/item2.html")

def itemselector3(request):
    get_client_ip(request)
    return render(request, f"mainpage/item3.html")

def itemselector4(request):
    get_client_ip(request)
    return render(request, f"mainpage/item4.html")

def contacts(request):
    get_client_ip(request)
    return render(request, "mainpage/contact_us.html")