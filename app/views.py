#!/usr/bin/python3
"""views module"""

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import User, Budget, Expense
from werkzeug.security import check_password_hash

user_collection = User()
expense_collection = Expense()


def index(request):
    """home page view"""
    return render(request, 'app/index.html')

def signup(request):
    """sign up page"""
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        new_user = user_collection.find_one({"email": email})
        if new_user and check_password_hash(new_user["password"], password):
            return render(request, 'app/index.html')

        user = user_collection.create_user(username, email, password)
        request.session["user_id"] = str(user["_id"])
        return render(request, 'app/no_budget.html', username)

    return render(request, 'app/index.html')

def login(request):
    """login page"""
    if request.method == "POST":
        # username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = user_collection.find_one({"email": email})

        if user and check_password_hash(user["password"], password):
            request.session["user_id"] = str(user["_id"])
            return render(request, 'app/dashboard.html', user["username"])
        
        return HttpResponse("error: invalid credentials")
    # return redirect(request, "homepage")
    return render(request, 'app/index.html')

def dashboard(request):
    """user dashboard"""
    return HttpResponse("Make a budget!")

def make_budget(request):
    """make new budget"""
    return render(request, 'app/make_budget.html')

def expense(request, budget_id):
    """capture new expense"""
    budget = get_object_or_404(Budget, id=budget_id)

    return render(request, 'app/expense.html', budget)

def create_expense(request, budget_id):
    """create new expense record"""
    if request.method == 'POST':
        category = request.POST.get("category")
        amount = request.POST.get("amount")
        
        budget = get_object_or_404(Budget, id=budget_id)
        expense_collection.create_expense(budget_id, category, amount)
        expenses = expense_collection.find({"budget_id": budget_id})

        total = 0
        largest = expenses[0]
        for expense in expenses:
            total += expense["amount"]
            if expense["amount"] > largest["amount"]:
                largest = expense
        
        category_name = largest["category"]
        return render(request, 'app/dashboard.html', {
            "total": total,
            "category_name": category_name
        })
    