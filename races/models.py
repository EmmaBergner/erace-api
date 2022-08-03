from django.db import models
from django.contrib.auth.models import User


class Race(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=False)
    distance = models.IntegerField(blank=False)
    country = models.TextField(blank=False)
    date = models.DateTimeField(auto_now_add=False)
    website = models.CharField(max_length=255, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.name}'
