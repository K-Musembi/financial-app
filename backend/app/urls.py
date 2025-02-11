#!/usr/bin/python3
"""urls for app"""

from django.urls import path
from . import views

app_name = "app"

urlpatterns = [
    path("budget_dashboard", views.budget_dashboard, name="budget_dashboard"),
    path("signup", views.signup, name="signup"),
    path("login", views.login, name="login"),
    path("createbudget", views.createbudget, name="createbudget"),
    path("addexpense", views.addexpense, name="addexpense"),
    path("logout", views.logout, name="logout"),
]
