from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('article_detail/<int:pk>/', views.article_detail, name='detail'),
    path('create_article/', views.create_article, name='create_article'),
]
