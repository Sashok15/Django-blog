from django.urls import path
from rest_framework.routers import DefaultRouter    
from rest_framework_swagger.views import get_swagger_view

from . import views
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register('polls', PollViewSet, base_name='polls')


# urlpatterns = [
#     # ...
# ]

# urlpatterns += router.urls
schema_view = get_swagger_view(title='Polls API')

urlpatterns = [
    path('articles/', views.ArticleList.as_view(), name='articles_list'),
    path('comments/', views.CommentList.as_view(), name='comments_list'),
    path('article/<int:pk>/detail/', views.ArticleDetail.as_view(), name='article_detail'),
    path('comment/<int:pk>/detail/', views.CommentDetail.as_view(), name='comment_detail'),
    path('create-article/', views.CreateArticle.as_view(), name='create_article_api'),
    path('create-user/', views.CreateUser.as_view(), name='create_user'),
    path('login/', views.LoginView.as_view(), name='api_login'),
    path('swagger-docs/', schema_view),
]