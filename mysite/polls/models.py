from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post")
    members = models.ManyToManyField(User, related_name="members", blank=True)

    def __str__(self):
        return self.title
