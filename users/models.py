import os

from PIL import Image
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.urls import reverse
from django.utils import timezone
from djangoProject import settings


def img_uploader(instance, image_name):
    image_name = 'user_images/{0}/profile.jpg'.format(instance.username)
    full_path = os.path.join(settings.MEDIA_ROOT, image_name)
    if os.path.exists(full_path):
        os.remove(full_path)
    return image_name


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, username, first_name, last_name, id_num, password, **extra_fields):
        if not email:
            raise ValueError('Se requiere correo')
        if not username:
            raise ValueError('Se requiere nombre de usuario')
        if not first_name:
            raise ValueError('Se requiere nombre completo')
        if not last_name:
            raise ValueError('Se requiere apellidos')
        if not id_num:
            raise ValueError('Se requiere número de identificación')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            id_num=id_num,
            last_login=timezone.now(),
            date_joined=timezone.now(),
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, username, first_name, last_name, id_num, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_admin', False)
        return self._create_user(email, username, first_name, last_name, id_num, password, **extra_fields)

    def create_superuser(self, email, username, first_name, last_name, id_num, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_admin', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser debe ser personal.')
        if extra_fields.get('is_admin') is not True:
            raise ValueError('Superuser debe ser admin.')

        return self._create_user(email, username, first_name, last_name, id_num, password, **extra_fields)


class Profile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, verbose_name='Correo electrónico', unique=True)
    username = models.CharField(max_length=28, verbose_name='Usuario', unique=True)
    first_name = models.CharField(max_length=80, verbose_name='Nombres')
    last_name = models.CharField(max_length=80, verbose_name='Apellidos')
    id_num = models.CharField(max_length=12, verbose_name='Número de identificación', unique=True)
    date_joined = models.DateTimeField(verbose_name="Fecha de creación", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="Último logueo", auto_now=True)
    profile_picture = models.ImageField(verbose_name="Foto", default="user.png", upload_to=img_uploader)

    is_active = models.BooleanField(verbose_name="Activo",
                                    help_text='Cambia el estado a activa e inactiva de la cuenta', default=True)
    is_admin = models.BooleanField(verbose_name="Administrador",
                                   help_text='Asigna a la cuenta privilegios de superusuario en el sistema',
                                   default=False)  # a superuser
    is_staff = models.BooleanField(verbose_name="Personal",
                                   help_text='Asigna a la cuenta privilegios relacionados de personal en el sistema',
                                   default=False)  # a admin user; non super-user

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'id_num', 'first_name', 'last_name']

    objects = UserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = "Usuarios"
        verbose_name = "Usuario"

    def get_full_name(self):
        # The user is identified by their email address
        return self.first_name

    def get_short_name(self):
        # The user is identified by their email address
        return self.username

    def last_name_initial(value):
        """
        Returns the first character of lastname in lowercase for a given name
        """
        last_name = value.split()[-1]  # get the last name from value
        return last_name[0].lower()  # get the first letter of last name in lower case

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
