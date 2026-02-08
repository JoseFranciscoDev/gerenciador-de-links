from django.db import models
from django.contrib.auth.models import User


class Link(models.Model):
    titulo = models.CharField(
        blank=False,
        null=False,
        verbose_name="Titulo do link",
    )
    url = models.CharField(
        blank=False,
        null=False,
        verbose_name="URL do link",
    )
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.titulo
