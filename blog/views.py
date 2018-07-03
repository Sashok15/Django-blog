from django.shortcuts import render
from .models import Article


def index(request):
    articles = Article.objects.all()
    print(articles)
    context = {'articles': articles}
    return render(request, 'blog/index.html', context=context)


def ArticleDetail(request, pk):
    pass


class ArticleList():
    pass


def create_article(request):
    if request.method == "GET":
        pass
    elif request.method == "POST":
        pass

def update_article(request):
    pass


def delete_article(request):
    pass


def create_comment(request):
    pass


def update_comment(request):
    pass


def delete_comment(request):
    pass
