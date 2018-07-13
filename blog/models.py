from django.db import models

from django.contrib.auth.models import AbstractUser, User
from django.utils import timezone


# class User(AbstractUser):
#     class Meta:
#         permissions = (('can_update', 'To provide updeta own article'))


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        permissions = (
            ('custom_can_update_article', 'To provide update own article'),
        )

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    pub_date = models.DateTimeField('date published', auto_now=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text
