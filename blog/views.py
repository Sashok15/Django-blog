from django.shortcuts import render, get_object_or_404
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
        context = {'article_detail': article, 'comments': comments}
        return render(request, template_name="blog/articleDetail.html", context=context)
    elif request.method == "POST":
        pass


@login_required
def create_article(request):
    if request.method == "GET":
        form = ArticleForm()
        return render(request, template_name='blog/createArticle.html', context={'form': form})
    elif request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            title = request.POST.get('title')
            text = request.POST.get('text')
            user = request.user
            query = Article(title=title, text=text, author=user)
            query.save()
            messages.info(request, 'Ви сторили ')
            return index(request)


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
