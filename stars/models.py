from django.db import models
from django.contrib.auth.models import User
from races.models import Race


class Star(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    race = models.ForeignKey(Race, on_delete=models.CASCADE, related_name='stars')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'race']

    def __str__(self):
        return f'Star [owner: {self.owner}, race: {self.race}]'
