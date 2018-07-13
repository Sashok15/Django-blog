from django import forms
from .models import Article, Comment


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'text']

    # def __init__(self, *args, **kwargs):
    #     self.user = kwargs.pop('author') 
    #     super().__init__(*args, **kwargs)

    # def save(self):
    #     article = super().save(commit=False)
    #     article.user = self.user
    #     article.save()
    #     return article

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
