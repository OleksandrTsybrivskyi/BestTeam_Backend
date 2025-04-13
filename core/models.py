from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_accessibility_user = models.BooleanField(default=False)
    join_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


class Location(models.Model):
    name = models.CharField(max_length=200)
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)

    ramps = models.BooleanField(default=False)
    tactile_elements = models.BooleanField(default=False)
    adapted_toilets = models.BooleanField(default=False)
    wide_entrance = models.BooleanField(default=False)
    visual_impairment_friendly = models.BooleanField(default=False)
    wheelchair_accessible = models.BooleanField(default=False)

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


class Proposal(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Пропозиція користувача {self.user.username}\
            Текст пропозиції: {self.comment}'
