from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser,PermissionsMixin
)
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.utils import timezone




class AccountManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, first_name, Contact_No, password=None, **extra_fields):
        values = [email, first_name, Contact_No]
        field_value_map = dict(zip(self.model.REQUIRED_FIELDS, values))
        for field_name, value in field_value_map.items():
            if not value:
                raise ValueError('The {} value must be set'.format(field_name))

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            first_name=first_name,
            Contact_No=Contact_No,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, first_name, Contact_No, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, first_name, Contact_No, password, **extra_fields)

    def create_superuser(self, email, first_name, Contact_No, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(email, first_name, Contact_No, password, **extra_fields)


# Create your models here.
class Users(AbstractBaseUser,PermissionsMixin):
    username = models.CharField(max_length = 150)
    first_name = models.CharField(max_length = 150)
    last_name = models.CharField(max_length = 150)
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    Contact_No = models.CharField(max_length=11)
    Address = models.TextField(max_length=150)    
    
   
    objects = AccountManager()

    USERNAME_FIELD = 'email'
    
    REQUIRED_FIELDS = ['first_name', 'Contact_No']   

    def get_full_name(self):
        return self.first_name + " " + self.last_name

    def get_address(self):
        return self.Address   

    def contact_number(self):
        return self.Contact_No

    def get_short_name(self):
        return self.first_name.split()[0]
