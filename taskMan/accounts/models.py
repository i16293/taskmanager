from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser, models.Model):
    icon = models.ImageField(
        upload_to='img/',
        verbose_name='アイコン',
        blank=True,
        
    )


