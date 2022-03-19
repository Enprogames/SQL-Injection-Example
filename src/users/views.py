# users/views.py

from django.shortcuts import render


# Create your views here.
def login(request):
    print("---------going to login page-----------")
    return render(request, "registration/login.html")

def dashboard(request):
    return render(request, "users/dashboard.html")
