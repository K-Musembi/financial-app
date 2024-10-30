#!/usr/bin/python3
"""views module"""

from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import User, Budget, Expense
from werkzeug.security import check_password_hash

user_collection = User()


def index(request):
    """home page view"""
    return HttpResponse("Welcome to Pesa Track!")
    # provide simple login form on this homepage, with redirect to sign up page html

def sign_up(request):
    """sign up page"""
    if request.method == "POST":
        username = request.POST.get("username")
        # email = request.POST.get("email")
        password = request.POST.get("password")

        new_user = user_collection.find_one({"name": username})
        if new_user and check_password_hash(new_user["password"], password):
            return HttpResponse("User already registered")
            # redirect to sign up page html

        user = user_collection.create_user(username, password)
        request.session["user_id"] = str(user["_id"])
        return HttpResponse("welcome to dashboard")

    return HttpResponse("Back to home page")

def login(request):
    """login page"""
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = user_collection.find_one({"name": username})

        if user and check_password_hash(user["password"], password):
            request.session["user_id"] = str(user["_id"])
            return HttpResponse("Welcome back to dashboard!")  # redirect to dashboard
        
        return HttpResponse("error: invalid credentials")
    # return redirect(request, "homepage")
    return HttpResponse("Back to home page!")

def dashboard(request):
    """user dashboard"""
    return HttpResponse("Make a budget!")
