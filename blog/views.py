from django.shortcuts import render, redirect
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib import messages

# Добавим декоратор для проверки авторизации
@login_required
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)

            # Используем текущего авторизованного пользователя
            myuser = request.user

            # Присваиваем пользователя автором поста
            post.author = myuser
            post.save()

            messages.success(request,"Предмет успешно выставлен на продажу")
            return HttpResponseRedirect('/')
        else:
            messages.error(request,"Произошла Ошибка")
            return HttpResponseRedirect('/post/')
    else:
        form = PostForm()
        return render(request, "shop/sale.html", {"form": form})


