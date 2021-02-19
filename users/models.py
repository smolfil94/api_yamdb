from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    class Roles(models.TextChoices):
        ADMIN = 'admin', _('admin')
        MODERATOR = 'moderator', _('moderator')
        USER = 'user', _('user')

    role = models.CharField(max_length=100, choices=Roles.choices, default=Roles.USER)
    bio = models.TextField(blank=True)

    email = models.EmailField(_('email address'), unique=True, blank=False)

    username = models.CharField(
        max_length=150,
        unique=True,
    )

    objects = CustomUserManager()

    @property
    def is_moderator(self):
        return self.role == self.Roles.MODERATOR

    @property
    def is_admin(self):
        return self.role == self.Roles.ADMIN
