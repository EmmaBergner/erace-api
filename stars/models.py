from django.db import models
from django.contrib.auth.models import User
from races.models import Race


class Star(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    race = models.OneToOneField(Race, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.owner} stars {self.race}'
