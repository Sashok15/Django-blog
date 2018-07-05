from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Article, Comment
from .forms import ArticleForm, CommentForm


def index(request):
    articles = Article.objects.all().order_by('-pub_date')
    paginator = Paginator(articles, 10)
    page = request.GET.get('page')
    context = {'articles': paginator.get_page(page)}
    return render(request, 'blog/index.html', context=context)


def article_detail(request, pk):
    if request.method == "GET":
        article = get_object_or_404(Article, pk=pk)
        comments = Comment.objects.filter(article_id=pk)
        form = CommentForm(initial={'title': 'My Title', 'text': 'Loren Ipsun'})
        context = {'article_detail': article, 'comments': comments, 'form': form}
        return render(request, template_name="blog/articleDetail.html", context=context)
    
    elif request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            path = request.path
            text = form.cleaned_data['text']
            user = request.user
            query = Comment(text=text, author=user, article_id=pk)
            query.save()
            messages.info(request, 'Ви створили Коментарій')
            return HttpResponseRedirect(path)


@login_required
def create_article(request):
    if request.method == "GET":
        form = ArticleForm(initial={'title': 'My Title', 'text': 'Loren Ipsun'})
        return render(request, template_name='blog/createArticle.html', context={'form': form})
    elif request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            text = form.cleaned_data['text']
            user = request.user
            query = Article(title=title, text=text, author=user)
            query.save()
            messages.info(request, 'Ви створили статтю')
            return HttpResponseRedirect('/')


@login_required
def update_article(request, pk):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            text = form.cleaned_data['text']
            Article.objects.filter(id=pk).update(title=title, text=text)
            return HttpResponseRedirect('/')
    else:
        article = Article.objects.get(pk=pk)
        form = ArticleForm(initial={'title': article.title, 'text': article.text})
        return render(request, template_name='blog/updateArticle.html', context={'form': form,
                                                                                 'article': article})


def delete_article(request, pk):
    if request.method == 'GET':
        Article.objects.filter(id=pk).delete()
        return HttpResponseRedirect('/')
    else:
        pass


def update_comment(request):
    pass


def delete_comment(request):
    pass
