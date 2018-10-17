from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.translation import ugettext, ugettext_lazy as _
from django.utils import timezone
#from .utils import Selects
# Create your models here.
class AccountManager(BaseUserManager):
    def create_user(self, cedula, password=None, **kwargs):
        if not cedula:
            raise ValueError('Users must have a valid cedula.')

        account = self.model(
            cedula=self.model.normalize_username(cedula)
        )

        account.set_password(password)
        account.save()

        return account

    def create_superuser(self, cedula, password, **kwargs):
        account = self.create_user(cedula, password, **kwargs)

        account.is_superuser = True
        account.is_staff = True
        account.save()

        return account



class Account(AbstractBaseUser, PermissionsMixin):
    cedula=models.CharField(verbose_name='cedula', max_length=8,null=False, blank=False, unique=True, primary_key=True)
    nombre=models.CharField(verbose_name='Nombres', null=False, blank=False, max_length=50)
    apellido=models.CharField(verbose_name='Apellidos', null=False, blank=False, max_length=50)
    fecha_naci=models.DateField(verbose_name='Fecha de Nacimento', null=True, blank=True)
    email=models.EmailField(verbose_name='Correo Electronico', null=True, blank=True,)
    is_active = models.BooleanField(verbose_name='active', default=True)
    is_staff = models.BooleanField(verbose_name='staff status', default=False)
    is_superuser = models.BooleanField(verbose_name='superuser status', default=False)
    date_joined = models.DateTimeField(verbose_name='date joined', default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    def __str__(self):
        return str(self.cedula)



    objects = AccountManager()

    USERNAME_FIELD = 'cedula'


    def get_full_name(self):
        return ' '.join([self.cedula, self.last_name])

    def get_short_name(self):
        return self.cedula
