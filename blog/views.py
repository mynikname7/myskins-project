from django.shortcuts import render
from .forms import PostForm
from .models import Post
from django.http import HttpResponseRedirect,HttpResponse



from django.shortcuts import render
from .forms import PostForm
from .models import Post
from django.http import HttpResponse

def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return HttpResponse("<h1>Твой предмет зарегистрирован</h1>")
        else:
            return HttpResponse("<h1>Ошибка валидации</h1>")
    else:
        form = PostForm()
        return render(request, "shop/sale.html", {"form": form})
