from django.shortcuts import render, redirect
from .forms import User_regist
from .models import MyUser
from django.http import HttpResponseRedirect, HttpResponse,HttpResponseNotFound
from django.contrib.auth import authenticate,login as user_login




def register(request):
    if request.method == "POST":
        form = User_regist(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]

            user = MyUser(email=email, password=password)
            user.save()
            print(123)
            request.session['user_id'] = user.id         # Создание сессии
            request.session['user_email'] = user.email
            return HttpResponseRedirect('/')
    else:
        form = User_regist()

    return render(request, "auth/reg.html", {"form": form})



def login_user(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user = MyUser.objects.get(email=email, password=password)

            request.session['user_id'] = user.id         # Создание сессии
            request.session['user_email'] = user.email


            return render(request,"shop/market.html")
        except MyUser.DoesNotExist:
            return render(request, "auth/login.html")

    return render(request, "auth/login.html")

