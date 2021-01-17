from django.db import models
from django.utils import timezone


# Create your models here.

class Pin(models.Model):
    title = models.CharField(max_length=150)
    author = models.ForeignKey('pinusers.PinUser', on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='uploads/', blank=True)
    url = models.URLField(blank=True, null=True)
    likes = models.IntegerField(default=0)
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Comment(models.Model):
    pin = models.ForeignKey(
        Pin, on_delete=models.CASCADE, related_name='comment')
    author = models.ForeignKey(
        'pinusers.PinUser', on_delete=models.CASCADE, related_name='user')
    content = models.TextField()
    created_at = models.DateField(default=timezone.now)

    def __str__(self):
        return f'{self.content}'
