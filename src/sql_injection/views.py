# sql_injection/views.py

from django.shortcuts import render


def index(request):
    return render(request, "sql_injection/index.html")
