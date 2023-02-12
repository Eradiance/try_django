from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username, password)
        user = authenticate(request, username=username, password=password)
        if user is None:
            context = {"error": "Invalid username or password."}
            return render(request, "accounts/login.html", context=context)
        login(request, user)
        return redirect('/')
    return render(request, "accounts/login.html")

def logout_view(request):

    context = {}
    return render(request, "accounts/logout.html", context=context)

def registr_view(request):

    context = {}
    return render(request, "accounts/register.html", context=context)