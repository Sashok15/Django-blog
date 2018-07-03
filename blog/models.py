from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()
    pub_date = models.DateTimeField('date published', default=timezone.now())

    def __str__(self):
        return self.id, self.title, self.text, self.author_id


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    pub_date = models.DateTimeField('date published',  default=timezone.now())

    def __str__(self):
        return self.text, self.article_id, self.author_id
