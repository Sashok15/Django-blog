from django.urls import path
from rest_framework.routers import DefaultRouter    
from rest_framework_swagger.views import get_swagger_view

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.ArticleListView.as_view(), name='index'),
    path('index/', views.ArticleListView.as_view(), name='index'),
    path('create-article/', views.create_article, name='create_article'),
    path('detail/<int:pk>/', views.article_detail, name='detail'),
    # path('article-detail-class/<int:pk>/', views.ArticleDetail.as_view(), name='detail'),
    path('article-detail/<int:pk>/update/', views.update_article, name='update_article'),
    path('delete-article/<int:pk>/', views.delete_article, name='delete_article'),
    path('article-detail/<int:article_pk>/delete-comment/<int:comment_pk>/', views.delete_comment, name='delete_comment'),
    path('article-detail/<int:article_pk>/update-commnet/<int:comment_pk>/', views.update_comment, name='update_comment'),
]
