import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Role:
        USER = 'user'
        ADMIN = 'admin'
        MODERATOR = 'moderator'

    email = models.EmailField(unique=True, blank=False)
    bio = models.TextField(blank=True)
    confirmation_code = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
    )

    @property
    def is_admin(self):
        self.role = self.Role.ADMIN or self.is_superuser

    @property
    def is_moderator(self):
        self.role = self.Role.MODERATOR

    def get_payload(self):
        pass
