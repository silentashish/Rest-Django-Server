from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """Helps Django work with a custom user model."""

    def create_user(self, email, name, password=None):
        """Creates a new user profile object."""

        if not email:
            raise ValueError('Users must have an email address.')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Creates and saves a new super-user."""

        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Represent a 'user profile' inside the application"""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Used to get a user's full name."""

        return self.name

    def get_short_name(self):
        """Used to get a user's short name."""

        return self.name

    def __str__(self):
        """Django uses this to convert the object to a string."""

        return self.email


class ProfilesFeedItem(models.Model):
    """Profile status update."""

    user_profile = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Returns the model as a string."""
        return self.status_text

    def getname(self):
        return self.user_profile.name

    def getemail(self):
        return self.user_profile.email

class ImageUploadField(models.Model):
    image=models.ImageField(upload_to='media',blank=False)
    user_profile=models.ForeignKey('UserProfile',on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        """return string whenever it is required"""
        return self.user_profile.name

class ImageField(models.Model):
    image=models.ImageField(upload_to='media',blank=False)

class CommentField(models.Model):
    """This field is used to add comment in post """
    comment=models.CharField(max_length=255)
    user_profile=models.ForeignKey('UserProfile',on_delete=models.CASCADE)
    created_on=models.DateTimeField(auto_now_add=True)
    post=models.ForeignKey('ProfilesFeedItem',on_delete=models.CASCADE,default="")

    def _str_(self):
        return self.user_profile.name

class TokenFiled(models.Model):
    token=models.CharField(max_length=256)
