# Generated by Django 3.2.9 on 2021-11-17 22:28

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Correo electrónico')),
                ('username', models.CharField(max_length=28, unique=True, verbose_name='Usuario')),
                ('first_name', models.CharField(max_length=80, verbose_name='Nombres')),
                ('last_name', models.CharField(max_length=80, verbose_name='Apellidos')),
                ('id_num', models.CharField(max_length=12, unique=True, verbose_name='Número de identificación')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='Último logueo')),
                ('profile_picture', models.ImageField(blank=True, default='user.png', upload_to=users.models.img_uploader, verbose_name='Foto')),
                ('is_active', models.BooleanField(default=True, help_text='Cambia el estado a activa e inactiva de la cuenta', verbose_name='Activo')),
                ('is_admin', models.BooleanField(default=False, help_text='Asigna a la cuenta privilegios de superusuario en el sistema', verbose_name='Administrador')),
                ('is_staff', models.BooleanField(default=False, help_text='Asigna a la cuenta privilegios relacionados de personal en el sistema', verbose_name='Personal')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
            },
            managers=[
                ('objects', users.models.UserManager()),
            ],
        ),
    ]