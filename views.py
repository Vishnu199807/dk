from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('post_list')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('post_list')


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('post_list')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


@login_required(login_url='login')
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})


@login_required(login_url='login')
def create_post(request):
    if request.method == 'POST':
        # Create a new post using the form data
        post = Post(
            title=request.POST['title'],
            description=request.POST['description'],
            image=request.FILES['image'],
            author=request.user
        )
        post.save()
        return redirect('post_list')
    return render(request, 'create_post.html')