from django.shortcuts import render

# Create your views here.

def mainpage(request):
    return render(request,"forth_task/mainpage.html")
def shoppage(request):
    return render(request,"forth_task/shop.html")
def cartpage(request):
    return render(request,"forth_task/cart.html")