from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


def create_user(request: HttpRequest):
    if request.method == "GET":
        form: UserCreationForm = UserCreationForm()
        return render(request, "create_user.html", context={"form": form})
    if request.method == "POST":
        form: UserCreationForm = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(
                request,
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password1"],
            )
            login(request, user)
            messages.success(request, "Usuário Criado com sucesso")
            return redirect("home")
    return render(request, "create_user.html", context={"form": form})


def login_view(request: HttpRequest):
    if request.method == "POST":
        if not request.POST.get("username") or not request.POST.get("password"):
            messages.error(request, "Faltou o usuário ou a senha")  
        user: User = authenticate(
            username=request.POST.get("username"),
            password=request.POST.get("password"),
        )
        if user:
            if user.is_active:
                login(request, user)
                messages.success(request, f"Usuario logado com sucesso: {user}")
            else:
                messages.error(request, f"Sua conta foi desabilitada: {user}")
    return redirect("home")
