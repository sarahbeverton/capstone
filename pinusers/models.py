from django.db import models
from django.contrib.auth.models import AbstractUser
from pins.models import Pin

# Create your models here.


class PinUser(AbstractUser):
    pins = models.ManyToManyField(Pin, blank=True, symmetrical=False)
    following = models.ManyToManyField('self', symmetrical=False, blank=True)
    profile_pic = models.ImageField(
        upload_to='uploads/', blank=True, null=True)

    def count_following(self):
        return self.following.count()

    def count_followers(self):
        return PinUser.objects.filter(following=self).count()
