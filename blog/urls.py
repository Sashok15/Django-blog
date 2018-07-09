from django.urls import path
from rest_framework.routers import DefaultRouter    
from . import views, api_views

# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register('polls', PollViewSet, base_name='polls')


# urlpatterns = [
#     # ...
# ]

# urlpatterns += router.urls

urlpatterns = [
    path('', views.ArticleListView.as_view(), name='index'),
    path('index/', views.ArticleListView.as_view(), name='index'),
    path('create-article/', views.create_article, name='create_article'),
    path('article-detail/<int:pk>/', views.article_detail, name='detail'),
    path('article-detail/<int:pk>/update/', views.update_article, name='update_article'),
    path('delete-article/<int:pk>/', views.delete_article, name='delete_article'),

    path('api/articles/', api_views.ArticleList.as_view(), name='articles_list'),
    path('api/comments/', api_views.CommentList.as_view(), name='comments_list'),
    path('api/article/<int:pk>/detail/', api_views.ArticleDetail.as_view(), name='article_detail'),
    path('api/comment/<int:pk>/detail/', api_views.CommentDetail.as_view(), name='comment_detail'),
    path('api/create-article/', api_views.CreateArticle.as_view(), name='create_article_api'),
    path('api/create-user/', api_views.CreateUser.as_view(), name='create_user'),
    path('api/login/', api_views.LoginView.as_view(), name='api_login')
]
