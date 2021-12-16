import uuid

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    MANAGER = settings.MANAGER_ROLE
    EMPLOYER = settings.EMPLOYER_ROLE
    ADMIN = settings.ADMIN_ROLE
    ROLE_CHOICES = [
        (MANAGER, settings.MANAGER_ROLE),
        (EMPLOYER, settings.EMPLOYER_ROLE),
        (ADMIN, settings.ADMIN_ROLE)
    ]

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    role = models.TextField(
        choices=ROLE_CHOICES,
        default=EMPLOYER,
        blank=False
    )
    confirmation_code = models.TextField(
        verbose_name='Код подтверждения',
        max_length=100,
        default=uuid.uuid4,
        null=True,
        editable=False,
    )

    @property
    def is_admin(self):
        return self.role == settings.ADMIN_ROLE or self.is_staff

    @property
    def is_manager(self):
        return self.role == settings.MANAGER_ROLE

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        return str(self.username)
