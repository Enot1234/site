from django.shortcuts import render, redirect
from .models import *
from .forms import *


def home(request):
    return render(request, "index.html")


def laborinfo(request):
    return render(request, "laborinfo.html")


def tariffs(request):
    return render(request, "tariffs.html")


def registerSchool(request):
    if request.method == "POST":
        form = RegSchool(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
        
        return redirect('organization', pk=post.id)
    else:
        form = RegSchool()

    return render(request, "register/RegisterSchool.html", {"model": form})


def regUser(request):
    if request.method == "POST":
        form = RegUser(request.POST)
    else:
        form = RegUser()

    return render(request, "register/RegisterUser.html", {"model": form})


def organization(request, pk):
    bd = school.objects.filter(id = pk)

    return render(request, "office/organization.html", {"model": bd})

