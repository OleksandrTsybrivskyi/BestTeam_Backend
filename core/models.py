from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_accessibility_user = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class Location(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    address = models.CharField(max_length=255)
    
    has_ramp = models.BooleanField(default=False)
    has_tactile_elements = models.BooleanField(default=False)
    has_adapted_toilet = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    
    rating = models.IntegerField(default=0)
    comment = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Відгук {self.user.username} для {self.location.name}"
