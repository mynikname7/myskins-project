from django.shortcuts import render
from blog.models import Post


def scrol(request):
    icons = {"Dragon Lore": 'img/240fx152f.png', "Safari Mesh": 'img/360fx360f.png'}
    skins = Post.objects.all()
    for skin in skins:
        skin.icon = icons.get(skin.nameteg,'img/default.png')
    print(skins)
    return render(request,'shop/market.html',{"skins":skins})