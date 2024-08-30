from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(max_length=50, unique=True, blank=True, null=True, default=None)
    profile_image = models.URLField(default='https://res.cloudinary.com/dcfi0p4p4/image/upload/v1724406864/placeholder_lcjcaw.png', blank=True)
