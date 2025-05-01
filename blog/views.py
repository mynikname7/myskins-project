from django.shortcuts import render, redirect
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse

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

            return HttpResponse("<h1>Твой предмет зарегистрирован</h1>")
        else:
            return HttpResponse("<h1>Ошибка валидации</h1>")
    else:
        form = PostForm()
        return render(request, "shop/sale.html", {"form": form})
