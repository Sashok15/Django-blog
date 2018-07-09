from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.ArticleListView.as_view(), name='index'),
    path('create_article/', views.create_article, name='create_article'),
    path('article_detail/<int:pk>/', views.article_detail, name='detail'),
    path('article_detail/<int:pk>/update/', views.update_article, name='update_article'),
    path('delete_article/<int:pk>/', views.delete_article, name='delete_article'),
]
