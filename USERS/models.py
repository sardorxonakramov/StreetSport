from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.core.validators import RegexValidator
from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = (
        ("admin", "Admin"),
        ("owner", "Owner"),
        ("manager", "Manager"),
        ("user", "User"),
    )

    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    phone = models.CharField(
        max_length=13,
        validators=[
            RegexValidator(
                regex=r"^\+998\d{9}$",
                message="Telefon raqam formati: +998901234567 bo'lishi kerak.",
            )
        ],
        help_text="Masalan: +998901234567",
    )

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default="user")
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "phone"]

    def __str__(self):
        return f"{self.email} ({self.role})"
