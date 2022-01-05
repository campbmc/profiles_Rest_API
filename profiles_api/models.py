from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """manager for user profiles"""

    def create_user(self, email, name, password=None):
      """create a new user profile"""
      if not email:
        raise ValueError('User must have an email address')

      email = se;f.normalize_email(email)
      user= self.model(email=email, name=name)

      user.set_password(password)
      user.save(using=self._db)

      return user

    def create_superuser(self, email, name, password):
       """create and save new super user with given details"""
       user = self.create_user(email, name, password)

       user.is_superuser = True
       user.is_staff = True
       user.save(using=self._db)



# Create your models here.
class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the systems"""
    email = models.EmailField(max_length=225, unique=True)
    name = models.CharField(max_length=225)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """retreive full name of user"""
        return self.name

    def get_short_name(self):
        """Retrieve short name """
        return self.name

    def __str___(self):
        """return string representation of user"""
        return self.email
