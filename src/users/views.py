# users/views.py

from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.urls import reverse
from users.forms import CustomUserCreationForm


def dashboard(request):
    if request.user.is_authenticated:
        return render(request, "users/dashboard.html")
    else:
        return redirect(reverse("login"))


def register(request):
    if request.method == "GET":
        return render(
            request, "users/register.html",
            {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("dashboard"))
