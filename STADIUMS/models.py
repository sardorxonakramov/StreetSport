from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify

User = get_user_model()


class Stadion(models.Model):
    STATUS_CHOICES = (
        ("open", "Ochilgan"),
        ("closed", "Yopilgan"),
        ("maintenance", "Tamirda"),
    )

    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={"role": "owner"},
        related_name="owned_stadions",
    )
    location = models.CharField(max_length=100)
    capacity = models.IntegerField(default=10)
    date_opened = models.DateField()
    image = models.ImageField(upload_to="stadions/", blank=True,null=True) # bu rasim ustida  ishlashim kerak
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="open")
    is_active = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.location})"


class ManagerStadion(models.Model):
    stadion = models.ForeignKey(
        Stadion, on_delete=models.CASCADE, related_name="managers"
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={"role": "manager"},
        related_name="managed_stadions",
    )
    assigned_at = models.DateTimeField(auto_now_add=True)
    approved_by_owner = models.BooleanField(default=False)  # Tasdiqlovchi owner

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} → {self.stadion.name}"


class StadionImage(models.Model):
    stadion = models.ForeignKey(
        Stadion, on_delete=models.CASCADE, related_name="images"
    )
    image = models.ImageField(upload_to="stadions/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for {self.stadion.name}"

