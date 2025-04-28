from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "main.html")
