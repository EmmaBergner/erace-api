from django.db import models
from django.contrib.auth.models import User


class Race(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True)
    dictance = models.TextField(blank=True)
    country = models.TextField(blank=True)
    date = models.TextField(blank=True)
    website = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.name}'
