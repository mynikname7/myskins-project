from django.db import models
from django.utils import timezone
from regist.models import MyUser


class Post(models.Model):
    category = models.CharField(max_length=30)
    nameteg = models.CharField(max_length=50)
    Degree = models.CharField(max_length=30)
    body = models.IntegerField()
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE)  # Поле автора!
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
        ]

    def __str__(self):
        return self.title
