#!/usr/bin/python3
"""urls for app"""

from django.urls import path
from . import views

app_name = "app"

urlpatterns = [
    path("", views.index, name="index"),
    path("signup_page", views.signup_page, name="signup_page"),
    path("login_page", views.login_page, name="login_page"),
    path("budgetdashboard", views.budget_dashboard, name="budget_dashboard"),
    path("signup", views.signup, name="signup"),
    path("login", views.login, name="login"),
    path("make_budget", views.make_budget, name="make_budget"),
    path("budgetdashboard/createbudget", views.createbudget, name="createbudget"),
    path("expense/<str:budgetid>", views.expense, name="expense"),
    path("budgetdashboard/addexpense/<str:budgetid>", views.addexpense, name="addexpense"),
    path("logout", views.logout, name="logout"),
]
