import os

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.utils import timezone
from djangoProject import settings


def img_uploader(instance, filename):
    profile_image_name = 'profile_images/userID_{0}/profile.jpg'.format(instance.user.id)
    full_path = os.path.join(settings.MEDIA_ROOT, profile_image_name)
    if os.path.exists(full_path):
        os.remove(full_path)
    return profile_image_name


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, username, first_name, last_name, id_num, profile_picture=None, password=None):
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
            last_login=timezone.now()
        )
        user.profile_picture = profile_picture
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, first_name, last_name, id_num, password, profile_picture=None):
        user = self.create_user(
            email,
            username=username,
            first_name=first_name,
            last_name=last_name,
            id_num=id_num,
            password=password
        )

        user.profile_picture = profile_picture
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, verbose_name='Correo electrónico', unique=True)
    username = models.CharField(max_length=28, verbose_name='Usuario', unique=True)
    first_name = models.CharField(max_length=80, verbose_name='Nombres')
    last_name = models.CharField(max_length=80, verbose_name='Apellidos')
    id_num = models.CharField(max_length=12, verbose_name='Número de identificación', unique=True)
    date_joined = models.DateTimeField(verbose_name="Fecha de creación", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="Último logueo", auto_now=True)
    profile_picture = models.ImageField(verbose_name="Foto", default="user.png", upload_to='profile_images', blank=True)

    is_active = models.BooleanField(verbose_name="Activo", default=True)
    is_admin = models.BooleanField(verbose_name="Administrador", default=False)  # a superuser
    is_staff = models.BooleanField(verbose_name="Personal", default=False)  # a admin user; non super-user

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'id_num', 'first_name', 'last_name']

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        # The user is identified by their email address
        return self.first_name

    def get_short_name(self):
        # The user is identified by their email address
        return self.username

    @staticmethod
    def has_perm(self, *args, **kwargs):
        return True

    @staticmethod
    def has_module_perms(self, *args, **kwargs):
        return True
