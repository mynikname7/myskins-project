from django.contrib.auth.models import AbstractUser
from django.db import models

class MyUser(AbstractUser):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'           # логин по email
    REQUIRED_FIELDS = ['username']     # username всё ещё обязателен (можно убрать, если переопределить)

    def __str__(self):
        return self.email
