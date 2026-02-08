from django.urls import path
from . import views

urlpatterns = [
    path("criar_link/", views.create_link, name="criar_link"),
    path("excluir_links/", views.excluir_all_links_view, name="excluir_links"),
    path("excluir_link/<int:id>/", views.excluir_link, name="excluir_link"),
]
