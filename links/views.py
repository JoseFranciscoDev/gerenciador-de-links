from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User, AnonymousUser
from .forms import LinkForm
from .models import Link


def home(request: HttpRequest):
    user: User | AnonymousUser = request.user
    if user.is_active:
        links = Link.objects.filter(user=user)[:10]
    else:
        links = None
    return render(
        request,
        "home.html",
        {"links": links},
    )


def excluir_all_links_view(request: HttpRequest) -> HttpResponseRedirect:
    user = request.user
    if request.method == "POST":
        links = Link.objects.filter(user=user)
        links.delete()
        return redirect("home")
    return redirect("home")


def create_link(request):
    if not request.user.is_active:
        return redirect("create_user")
    if request.method == "POST":
        form = LinkForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            Link.objects.create(
                titulo=form.cleaned_data["titulo"],
                url=form.cleaned_data["url"],
                user=request.user,
            )
            messages.success(request, "Link salvo com sucesso ")
            return redirect("home")
    return render(
        request,
        "links/create_link.html",
    )


def excluir_link(request, id):
    link = Link.objects.filter(id=id)
    link.delete()
    messages.success(request, "Link deletado")
    return redirect("home")
