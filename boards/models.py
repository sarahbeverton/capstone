from django.db import models
from django.utils import timezone
from pinusers.models import PinUser
from pins.models import Pin
# Create your models here.

class Board(models.Model):
    user = models.ForeignKey(PinUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    pins = models.ManyToManyField(Pin, blank=True, symmetrical=False)

    def __str__(self):
        return self.title
