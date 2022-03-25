# users/views.py

from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.urls import reverse
from users.forms import CustomUserCreationForm
from django.contrib.auth.models import User
from users.models import Document

from django.http import HttpResponse


def detail(request, document_id):
    if request.user.is_authenticated:
        document = Document.objects.get(pk=document_id)
        context = {
            "title": document.title,
            "content": document.content
        }
        return render(request, "users/detail.html", context)
    else:
        return redirect(reverse("login"))


def dashboard(request):
    if request.user.is_authenticated:
        context = {
            "document_list": [{"id": document.id, "title": document.title} for document in request.user.document_set.all()]
        }
        return render(request, "users/dashboard.html", context)
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
