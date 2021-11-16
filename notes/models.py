from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from djangoProject import settings


# Board Model

class Board(models.Model):
    name = models.CharField(verbose_name="Nombre", max_length=150)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.PROTECT)
    public = models.BooleanField(default=False)
    private = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-updated_at']
        verbose_name_plural = "Tableros"
        verbose_name = "Tablero"


# Ideas Model

class Ideas(models.Model):
    board = models.ForeignKey(Board, on_delete=models.PROTECT, related_name="ideas")
    title = models.CharField(max_length=150)
    content = models.CharField(max_length=500)

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='ideas'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "Ideas"
        verbose_name = "Ideas"

    def save(self, *args, **kwargs):
        return super(Ideas, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('ideas',
                       args=[self.title])
