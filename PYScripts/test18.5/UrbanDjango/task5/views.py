from django.shortcuts import render
from .forms import registration_form

# Create your views here.
def sign_up_by_django(request):
    users = ["id1", "Boise", "Nigel"]
    info = {}
    if request.method == "POST":
        form = registration_form(request.POST)
        if form.is_valid():
            name = form.cleaned_data["username"]
            age = form.cleaned_data["age"]
            psw = form.cleaned_data["psw"]
            psw_repeat = form.cleaned_data["psw-repeat"]
            for user in users:
                if user == name:
                    info["error"] = "Пользователь уже существует"
                    info["form"] = form
                    return render(request, "fifth_task/registration_page.html", info)
            if int(age):
                info["error"] = "Возраст меньше 18"
                info["form"] = form
                return render(request, "fifth_task/registration_page.html", info)
            if psw != psw_repeat:
                info["error"] = "Пароли не совпадают"
                info["form"] = form
                return render(request, "fifth_task/registration_page.html", info)
            info["user"] = name
            info["form"] = form
            return render(request, "fifth_task/registration_page.html", info)
    else:
        form = registration_form()
        return render(request, "fifth_task/registration_page.html",{"form":form})

def sign_up_by_html(request):
    users = ["id1","Boise","Nigel"]
    info = {}
    if request.method == "POST":
        name = request.POST.get("username")
        age = request.POST.get("age")
        psw = request.POST.get("psw")
        psw_repeat = request.POST.get("psw-repeat")
        for user in users:
            if user == name:
                info["error"] = "Пользователь уже существует"
                return render(request,"fifth_task/registration_page.html",info)
        if int(age) < 18:
            info["error"] = "Возраст меньше 18"
            return render(request, "fifth_task/registration_page.html", info)
        if psw != psw_repeat:
            info["error"] = "Пароли не совпадают"
            return render(request, "fifth_task/registration_page.html", info)
        info["usr"] = name
        return render(request, "fifth_task/registration_page.html", info)
    else:
        return render(request, "fifth_task/registration_page.html")

