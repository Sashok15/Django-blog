from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from .views import signup, main_user_page
app_name = 'auth_app'
urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='auth_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('main/', main_user_page, name='main_user_page'),
    url(r'^reset/$',
        auth_views.PasswordResetView.as_view(
            template_name='auth_app/password_reset.html',
            email_template_name='auth_app/password_reset_email.html',
            subject_template_name='auth_app/password_reset_subject.txt',
            success_url='done/',
            # success_url=reverse_lazy('auth_app/password_reset_done'),
        ),
        name='password_reset'),
    url(r'^reset/done/$',
        auth_views.PasswordResetDoneView.as_view(template_name='auth_app/password_reset_done.html'),
        name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(template_name='auth_app/password_reset_confirm.html'),
        name='password_reset_confirm'),
    url(r'^reset/complete/$',
        auth_views.PasswordResetCompleteView.as_view(template_name='auth_app/password_reset_complete.html'),
        name='password_reset_complete'),
    #
    url(r'^settings/password/$',
        auth_views.PasswordChangeView.as_view
        (template_name='auth_app/password_change.html',
         success_url='done/'
         ),
        name='password_change'),
    url(r'^settings/password/done/$',
        auth_views.PasswordChangeDoneView.as_view(template_name='auth_app/password_change_done.html'),
        name='password_change_done'),
]
