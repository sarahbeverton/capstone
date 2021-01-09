from django.db import models
from django.contrib.auth.models import AbstractUser
from pins.models import Pin

# Create your models here.


class PinUser(AbstractUser):
    pins = models.ManyToManyField(Pin, blank=True, symmetrical=False)


class Profile(models.Model):
    user_following = models.ForeignKey(
        PinUser, related_name='users_following', null=True, on_delete=models.CASCADE)
    user_followers = models.ForeignKey(
        PinUser,
        related_name='user_followers', on_delete=models.CASCADE
    )
