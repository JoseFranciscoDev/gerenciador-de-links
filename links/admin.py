from django.contrib import admin
from .models import Link


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ["titulo", "url", "user"]
    fieldsets = [
        (
            "Informações Básicas",
            {
                "classes": ["wide"],
                "fields": ["titulo", "url", "user"],
            },
        )
    ]
