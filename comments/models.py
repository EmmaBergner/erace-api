from django.db import models
from django.contrib.auth.models import User
from races.models import Race


class Comment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    race = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(
        upload_to='image/', default='../default_profile_ko4ixg.jpg'
    )

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.text