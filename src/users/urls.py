# users/urls.py

from django.urls import path, include
from users import views

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("register/", views.register, name="register"),
    path('<int:document_id>/', views.detail, name='detail')
]
