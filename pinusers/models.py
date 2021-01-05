from django.db import models
from django.contrib.auth.models import AbstractUser
from pins.models import Pin

# Create your models here.

class PinUser(AbstractUser):
    pins = models.ManyToManyField(Pin, blank=True, symmetrical=False)
