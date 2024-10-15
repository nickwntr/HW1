from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def sign_up_by_html(request):
    info = {}
    if request.method == "POST":
        name = request.POST.get("username")
        age = request.POST.get("age")
        psw = request.POST.get("psw")
        psw_repeat = request.POST.get("psw-repeat")
        users = Buyer.objects.all()
        for user in users:
            if user.name == name:
                info["error"] = "Пользователь уже существует"
                return render(request,"forth_task/registration_page.html",info)
        if int(age) < 18:
            info["error"] = "Возраст меньше 18"
            return render(request, "forth_task/registration_page.html", info)
        if psw != psw_repeat:
            info["error"] = "Пароли не совпадают"
            return render(request, "forth_task/registration_page.html", info)
        Buyer.objects.create(name=name,age=age)
        return redirect('/')
    else:
        return render(request, "forth_task/registration_page.html")

def mainpage(request):
    return render(request,"forth_task/mainpage.html")
def shoppage(request):
    games = Game.objects.all()
    return render(request,"forth_task/shop.html",{"games":games})
def cartpage(request):
    return render(request,"forth_task/cart.html")