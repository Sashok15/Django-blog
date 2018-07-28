from django.db import models

from django.contrib.auth.models import AbstractUser, User
from django.urls import reverse
from django.utils import timezone


# class User(AbstractUser):
#     class Meta:
#         permissions = (('can_update', 'To provide updeta own article'))

def upload_location(instance, filename):
    return "media_collected/"


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image = models.ImageField(null=True,
                              blank=True,
                              width_field='width_field',
                              height_field='height_field')
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    text = models.TextField()
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        permissions = (
            ('custom_can_update_article', 'To provide update own article'),
        )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={"pk": self.id})


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    pub_date = models.DateTimeField(
        'date published', auto_now=False, auto_now_add=True)
    update = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.text
