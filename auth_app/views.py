from django.shortcuts import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, \
    login as auth_login
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
from blog.models import Article


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = SignUpForm()
    return render(request, 'auth_app/signup.html', {'form': form})


@login_required(redirect_field_name='login')
def main_user_page(request):
    orders = Article.objects.filter(user=request.user.id)
    context = {'orders': orders}
    return render(request, 'auth_app/main_user_page.html', context)
