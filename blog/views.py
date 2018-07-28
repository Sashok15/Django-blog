from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, Http404, redirect
from django.views import generic, View

from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from .permissions import has_perm_or_is_author


class ArticleListView(generic.ListView):
    model = Article
    paginate_by = 3
    context_object_name = 'articles'
    template_name = 'blog/index.html'
    def get_queryset(self):
        queryset = Article.objects.all().order_by('-pub_date')
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) |
                Q(text__icontains=query)
            )
        return queryset

# class ArticleDetail(generic.DetailView):

#     model = Article
#     context_object_name = 'articles'
#     template_name = 'blog/articleDetail.html'

#     def get(self, request, *args, **kwargs):
#         form = CommentForm(initial={'title': 'My Title', 'text': 'Loren Ipsun text'})

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['comments'] = Comment.objects.filter(article_id=id).order_by("-pub_date")


def article_detail(request, pk):
    if request.method == "GET":
        article = get_object_or_404(Article, pk=pk)
        comments = Comment.objects.filter(article_id=pk).order_by("-pub_date")
        form = CommentForm(
            initial={'title': 'My Title', 'text': 'Loren Ipsun text'})
        is_owner = has_perm_or_is_author(
            user_object=request.user, instance=article)
        context = {'article': article, 'comments': comments,
                   'form': form, 'is_owner': is_owner}
        return render(request, template_name="blog/articleDetail.html", context=context)
    elif request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            user = request.user
            query = Comment(text=text, author=user, article_id=pk)
            query.save()
            messages.info(request, 'Ви створили Коментарій')
            return redirect('blog:detail', pk=pk)


@login_required
def create_article(request):
    if request.method == "GET":
        form = ArticleForm(
            initial={'title': 'My Title', 'text': 'Loren Ipsun'})
        return render(request, template_name='blog/createArticle.html', context={'form': form})
    elif request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            query = form.save(commit=False)
            # title = form.cleaned_data['title']
            # text = form.cleaned_data['text']
            query.author = request.user
            # query = Article(title=title, image=img, text=text, author=user)
            query.save()
            messages.info(request, 'Ви створили статтю')
            return redirect('blog:index')


@permission_required('blog.custom_can_update_article')
@login_required
def update_article(request, pk):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            query = form.save(commit=False)
            query.author = request.user
            query.title = form.cleaned_data['title']
            query.text = form.cleaned_data['text']
            query.image = form.cleaned_data['image']
            query.save()
            # Article.objects.filter(id=pk).update(title=title, text=text)
            return redirect('blog:index')
    else:
        article = Article.objects.get(pk=pk)
        has_perm = has_perm_or_is_author(request.user, article)
        if has_perm:
            form = ArticleForm(
                initial={'title': article.title, 'text': article.text})
            return render(request, template_name='blog/updateArticle.html', context={'form': form,
                                                                                     'article': article})
        else:
            raise Http404


@login_required
def delete_article(request, pk):
    if request.method == 'POST':
        Article.objects.filter(id=pk).delete()
        return redirect('blog:index')
    else:
        raise Http404

# @login_required(redirect_field_name='/admin/')
@login_required
def update_comment(request, article_pk, comment_pk):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            Comment.objects.filter(id=comment_pk).update(text=text)
            return redirect('blog:detail', pk=article_pk)
    else:
        article = Article.objects.get(pk=article_pk)
        comment = Comment.objects.get(pk=comment_pk)
        has_perm = has_perm_or_is_author(request.user, comment)
        if has_perm:
            form = CommentForm(initial={'text': comment.text})
            return render(request, template_name='blog/updateComment.html', context={'form': form,
                                                                                     'article': article,
                                                                                     'comment': comment})
        else:
            raise Http404


# @login_required(redirect_field_name='/admin/')
@login_required
def delete_comment(request, article_pk, comment_pk):
    if request.method == 'POST':
        Comment.objects.filter(id=comment_pk).delete()
        return redirect('blog:detail', pk=article_pk )
    else:
        raise Http404