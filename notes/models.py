import uuid
from datetime import datetime, timezone
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.functions import datetime
from django.urls import reverse

from djangoProject import settings

User = get_user_model()


# Board Model

class Board(models.Model):
    STATUS_CHOICES = (
        ('publico', 'Público'),
        ('privado', 'Privado'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, help_text='ID único para el tablero',
                          max_length=36)
    name = models.CharField(verbose_name="Nombre", max_length=150)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.PROTECT, verbose_name="Usuario")
    status = models.CharField(max_length=7, choices=STATUS_CHOICES, default='privado', blank=True, verbose_name="Estado",
                              help_text='Visibilidad del tablero')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Última actualización")

    def __str__(self):
        return f'{self.name}'

    def older_than_a_min(self):
        return (datetime.datetime.now(timezone.utc) - self.updated_at).seconds < 60

    @staticmethod
    def timereference():
        return datetime.datetime.now(timezone.utc)

    class Meta:
        ordering = ['-updated_at']
        verbose_name_plural = "Tableros"
        verbose_name = "Tablero"

    def get_absolute_url(self):
        return reverse('board', kwargs={"id": self.id})


# Ideas Model

class Ideas(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE, verbose_name="Tablero")
    title = models.CharField(max_length=150, verbose_name="Título")
    content = models.TextField(max_length=500, verbose_name="Contenido")
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="Usuario")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Última módificación")

    def __str__(self):
        return f'{self.title} ({self.board.name})'

    class Meta:
        ordering = ['-updated_at']
        verbose_name_plural = "Ideas"
        verbose_name = "Idea"

    def get_absolute_url(self):
        return reverse('board', kwargs={"id": self.board_id})
