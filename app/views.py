#!/usr/bin/python3
"""views module"""

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import User, Budget, Expense
from werkzeug.security import check_password_hash
from django.contrib import messages

user_collection = User()
expense_collection = Expense()
budget_collection = Budget()


def index(request):
    """home page view"""
    user_id = request.session.get("user_id")

    if user_id:
        return redirect("app:dashboard")
    
    return render(request, 'app/index.html')

def signup_page(request):
    """return signup page"""
    return render(request, 'app/signup.html')

def login_page(request):
    """return login page"""
    return render(request, 'app/login.html')

def signup(request):
    """sign up page"""
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        new_user = user_collection.find_one({"email": email})
        
        if not new_user:
            user = user_collection.create_user(username, email, password)
            # 'user.inserted_id' is for new document. After, use 'user._id'
            request.session["user_id"] = str(user.inserted_id)
            
            return redirect("app:dashboard")
        else:
            messages.error(request, "email already registered!")

    return redirect("app:signup_page")

def login(request):
    """login page"""
    if request.method == "POST":
        # username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = user_collection.find_one({"email": email})

        if user and check_password_hash(user["password"], password):
            request.session["user_id"] = str(user["_id"])
            # username = user["username"]
            return redirect("app:dashboard")
        else:
            messages.error(request, "invalid credentials")
        
    return redirect("app:login_page")

def dashboard(request):
    """user dashboard"""
    from bson import ObjectId

    user_id = request.session.get("user_id")

    if not user_id:
        return redirect("app:login_page")
    
    # default id in the PyMongo database is of type ObjectID
    user_id = ObjectId(user_id)
    user = user_collection.find_one({"_id": user_id})
    username = user["name"]
    budgets = budget_collection.find({"user_id": user_id})

    for budget in budgets:
        budget["budgetid"] = str(budget["_id"])

    return render(request, "app/dashboard.html", {
        "username": username.capitalize(),
        "budgets": budgets
    })

def make_budget(request):
    """make new budget"""
    user_id = request.session.get("user_id")

    if not user_id:
        return redirect("app.login")
    
    return render(request, 'app/make_budget.html')

def create_budget(request):
    """create new budget record / document"""
    from bson import ObjectId

    if request.method == 'POST':
        user_id = request.session.get("user_id")
        time_period = request.POST.get('time_period')
        amount = request.POST.get('amount')

        user_id = ObjectId(user_id)
        total_expenditure = 0
        budget_collection.create_budget(
            user_id, time_period, amount, total_expenditure)

        messages.success(request, "Budget created successfully!")
        return redirect("app:dashboard")

    return redirect("app:index")

def expense(request, budgetid):
    """capture new expense"""
    # budget = get_object_or_404(Budget, id=budget_id)
    # budget = budget_collection.find_one({"_id": budget_id})

    return render(request, 'app/expense.html', {"budgetid": budgetid})

def new_expense(request, budgetid):
    """create new expense record"""
    from bson import ObjectId

    if request.method == 'POST':
        category = request.POST.get("category")
        amount = request.POST.get("amount")
    
        expense_collection.create_expense(budgetid, category, amount)
        budget = budget_collection.find_one({"_id": ObjectId(budgetid)})
        # expenses = expense_collection.find({"budget_id": budget_id})

        if budget:
            total_expenditure = budget.get("total_expenditure", 0)
            total_expenditure += amount

            budget_collection.update(
                {"_id": ObjectId(budgetid)}, {"total_expenditure": total_expenditure})
    
            return redirect("app:dashboard")
        else:
            return redirect("app:dashboard")
 
    return redirect("app:index")

def logout(request):
    """log out user"""
    request.session.flush()

    messages.success(request, "You have successfully logged out!")
    return redirect("app:index")
    