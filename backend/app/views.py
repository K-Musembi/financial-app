#!/usr/bin/python3
"""views module"""

# from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import User, Budget, Expense
from werkzeug.security import check_password_hash
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
import json

user_collection = User()
expense_collection = Expense()
budget_collection = Budget()


@csrf_exempt
def signup(request):
    """sign up page"""
    if request.method == "POST":
        # if using formData in React, use request.POST.get("email")

        # when using JSON.stringify in React:
        data = json.loads(request.body)
        username = data.get("username")
        email = data.get("email")
        password = data.get("password")

        new_user = user_collection.find_one({"email": email})
        
        if not new_user:
            user = user_collection.create_user(username, email, password)
            # 'user.inserted_id' is for new document. After, use 'user._id'
            request.session["user_id"] = str(user.inserted_id)
            return HttpResponse(status=200)
        else:
            messages.error(request, "email already registered!")

    return HttpResponse(status=401)

@csrf_exempt
def login(request):
    """login page"""
    if request.method == "POST":
        # if using formData in React, use request.POST.get("email")
        data = json.loads(request.body)
        email = data.get("email")
        password = data.get("password")

        user = user_collection.find_one({"email": email})

        if user and check_password_hash(user["password"], password):
            request.session["user_id"] = str(user["_id"])
            return HttpResponse(status=200)
        else:
            messages.error(request, "invalid credentials")
    return HttpResponse(status=403)

@csrf_exempt
def budget_dashboard(request):
    """user dashboard"""
    from bson import ObjectId

    user_id = request.session.get("user_id")

    if not user_id:
        return HttpResponse(status=401)
    
    # default id in the PyMongo database is of type ObjectID
    user_id = ObjectId(user_id)
    user = user_collection.find_one({"_id": user_id})
    username = user["name"]
    budgets = budget_collection.find({"user_id": user_id})

    for budget in budgets:
        budget["budgetid"] = str(budget["_id"])
        budget["_id"] = str(budget["_id"])
        budget["user_id"] = str(budget["user_id"])
    
    data = {
        "username": username.capitalize(),
        "budgets": budgets
    }

    return JsonResponse(data, status=200)


@csrf_exempt
def createbudget(request):
    """create new budget record / document"""
    from bson import ObjectId

    if request.method == 'POST':
        user_id = request.session.get("user_id")
        data = json.loads(request.body)
        time_period = data.get('timePeriod')
        amount = data.get('amount')

        user_id = ObjectId(user_id)
        total_expenditure = 0
        budget_collection.create_budget(
            user_id, time_period, amount, total_expenditure)

        messages.success(request, "Budget created successfully!")
        # return redirect("app:budget_dashboard")
        return HttpResponse(status=200)

    return HttpResponse(status=401)

# def addexpense(request, budgetid):
@csrf_exempt
def addexpense(request):
    """create new expense record"""
    from bson import ObjectId

    if request.method == 'POST':
        data = json.loads(request.body)
        category = data.get("category")
        amount = data.get("amount")
        budgetid = data.get("budgetid")
    
        expense_collection.create_expense(budgetid, category, amount)
        budget = budget_collection.find_one({"_id": ObjectId(budgetid)})
        # expenses = expense_collection.find({"budget_id": budget_id})

        if budget:
            total_expenditure = budget.get("total_expenditure", 0)
            total_expenditure += int(amount)

            budget_collection.update(
                {"_id": ObjectId(budgetid)}, {"total_expenditure": total_expenditure})

            # return redirect("app:budget_dashboard")
            return HttpResponse(status=200)
        else:
            # return redirect("app:budget_dashboard")
            return HttpResponse(status=401)
 
    return HttpResponse(status=401)


@csrf_exempt
def logout(request):
    """log out user"""
    request.session.flush()
    messages.success(request, "You have successfully logged out!")
    return HttpResponse(status=200)
    