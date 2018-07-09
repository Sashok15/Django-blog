from django.shortcuts import render, get_object_or_404, Http404
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.views import generic

from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from .permissions import has_perm_or_is_author


class ArticleListView(generic.ListView):
    model = Article
    queryset = Article.objects.all().order_by('-pub_date')
    paginate_by = 10
    context_object_name = 'articles'
    template_name = 'blog/index.html'

def article_detail(request, pk):
    if request.method == "GET":
        article = get_object_or_404(Article, pk=pk)
        comments = Comment.objects.filter(article_id=pk).order_by("-pub_date")
        form = CommentForm(initial={'title': 'My Title', 'text': 'Loren Ipsun'})
        is_owner = False
        if request.user.id == article.author_id:
            is_owner = True
        context = {'article_detail': article, 'comments': comments, 'form': form, 'is_owner': is_owner}
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


@permission_required('blog.custom_can_update_article')
@login_required
def update_article(request, pk):
    if request.method == 'PUT':
        form = ArticleForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            text = form.cleaned_data['text']
            Article.objects.filter(id=pk).update(title=title, text=text)
            return HttpResponseRedirect('/')
    else:
        article = Article.objects.get(pk=pk)
        if request.user.id != article.author_id:
            raise Http404
        form = ArticleForm(initial={'title': article.title, 'text': article.text})
        return render(request, template_name='blog/updateArticle.html', context={'form': form,
                                                                                 'article': article})


@login_required
def delete_article(request, pk):
    if request.method == 'POST':
        Article.objects.filter(id=pk).delete()
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')


# only admin do it
@login_required(redirect_field_name='/admin/')
def edit_comment(request):
    pass


@login_required(redirect_field_name='/admin/')
def delete_comment(request):
    pass
