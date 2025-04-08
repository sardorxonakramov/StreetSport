from django.db import models
from STADIUMS.models import Stadion
from django.contrib.auth import get_user_model

User =get_user_model()

class StadionBooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stadion = models.ForeignKey(Stadion, on_delete=models.CASCADE)
    booking_time = models.DateTimeField(auto_now_add=True)
    is_offline = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['stadion'], 
                condition=models.Q(is_active=True), 
                name='unique_active_booking'
            )
        ]

    def __str__(self):
        return f"{self.stadion.name} → {self.user.email} ({'offline' if self.is_offline else 'online'})"
