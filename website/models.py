from django.db import models
from django.urls import reverse


class Contact(models.Model):
    fullname = models.CharField(max_length=120, verbose_name="Nombre completo")
    email = models.EmailField(verbose_name="Correo electrónico")
    subject = models.CharField(verbose_name="Asunto", max_length=50)
    message = models.TextField(verbose_name="Mensaje", max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at']
        verbose_name_plural = "Preguntas"
        verbose_name = "Pregunta"

    def __str__(self):
        return f'{self.subject}'


class Feedback(models.Model):
    response = models.TextField(verbose_name="Respuesta")
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at']
        verbose_name_plural = "Respuestas"
        verbose_name = "Respuesta"

    def __str__(self):
        return f'{self.response}'

