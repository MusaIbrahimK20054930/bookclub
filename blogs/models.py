from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    first_name = models.CharField(max_length = 50, blank = False)
    last_name = models.CharField(max_length = 50, blank = False)
    email = models.EmailField(unique = True, blank = False)
    bio = models.TextField(max_length = 500, blank = True)
