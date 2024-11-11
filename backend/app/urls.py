#!/usr/bin/python3
"""urls for app"""

from django.urls import path
from . import views

app_name = "app"

urlpatterns = [
    path("", views.index, name="index"),
    path("signup_page", views.signup_page, name="signup_page"),
    path("login_page", views.login_page, name="login_page"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("signup", views.signup, name="signup"),
    path("login", views.login, name="login"),
    path("make_budget", views.make_budget, name="make_budget"),
    path("create_budget", views.create_budget, name="create_budget"),
    path("expense/<str:budgetid>", views.expense, name="expense"),
    path("new_expense/<str:budgetid>", views.new_expense, name="new_expense"),
    path("logout", views.logout, name="logout"),
]
