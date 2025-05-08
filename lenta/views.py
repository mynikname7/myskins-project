from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post
from django.core.paginator import Paginator


def scrol(request):
    icons = {"Dragon Lore": 'img/240fx152f.png', "Safari Mesh": 'img/360fx360f.png'}
    post_list = Post.objects.all()
    paginator = Paginator(post_list,3)
    page_number = request.GET.get("page",1)
    page_obj = paginator.get_page(page_number)
    for skin in page_obj:
        skin.icon = icons.get(skin.nameteg.strip(),'img/default.png')
    for i in page_obj:
        print(i.icon)
    return render(request,'shop/market.html',{'page_obj': page_obj})

def buy_item(request):
    if request.method == "POST":
        return HttpResponse("<h1>Хорош</h1>")

    return render(request,'shop/buy.html')