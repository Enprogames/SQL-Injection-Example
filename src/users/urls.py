# users/urls.py

from django.urls import path, include
from users import views

urlpatterns = [
    path("", views.login, name="login"),
    path("accounts/", include("django.contrib.auth.urls")),
]
