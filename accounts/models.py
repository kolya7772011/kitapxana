from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    role_choices = (
        ('kitapxanashi', 'Kitapxanashi'),
        ('oqiwshi', 'Oqiwshi'),
    )

    role = models.CharField(max_length=200,choices=role_choices,default='kitapxanashi')

