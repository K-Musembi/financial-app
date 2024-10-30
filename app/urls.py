#!/usr/bin/python3
"""urls for app"""

from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("sign_up/", views.sign_up, name="sign_up"),
    path("login/", views.login, name="login"),
    path("dashboard/", views.dashboard, name="dashboard"),
]
