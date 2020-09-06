import uuid
import os
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                        PermissionsMixin, User
from django.conf import settings


# class UserManager(BaseUserManager):
#
#     def create_user(self, email, password=None, **extra_fields):
#         """Creates and save a user"""
#         if not email:
#             raise ValueError("Users must have an email address")
#         user = self.model(email=self.normalize_email(email), **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#
#         return user
#
#     def create_superuser(self, email, password):
#         """Creates and saves a new superuser"""
#         user = self.create_user(email, password)
#         user.is_staff = True
#         user.is_superuser = True
#         user.save(using=self._db)
#
#         return user


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpeg', upload_to='profile_pics')

    def __str__(self):
        return f"{self.user.username} Profile"
