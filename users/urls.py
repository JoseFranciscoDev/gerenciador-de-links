from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_view, name="login_view"),
    path("create_user/", views.create_user, name="create_user"),
]
