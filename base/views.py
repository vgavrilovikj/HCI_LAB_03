from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.models import User
from .models import Post, Comment, UserInfo
from .forms import PostForm, UserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q


# Create your views here.
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            print("User does not exist")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

    context = {}
    return render(request, 'login.html', context)


@login_required(login_url='login')
def profilePage(request, pk):
    user = User.objects.get(id=pk)
    context = {'user': user}
    return render(request, 'profile.html', context)


@login_required(login_url='login')
def editProfile(request, pk):
    user = User.objects.get(id=pk)
    userInfo = UserInfo.objects.get(user=user)
    form = UserForm(instance=userInfo)

    if request.method == 'POST':
        if request.user.id == user.id:
            form = UserForm(request.POST, instance=userInfo)
            if form.is_valid():
                form.save()
                return redirect('home')

    context = {'form': form}
    return render(request, 'profile-form.html', context)


def home(request):
    q = request.GET.get('q') if request.GET.get('q') is not None else ''
    posts = Post.objects.filter(Q(title__contains=q) | Q(text__contains=q))
    context = {'posts': posts}
    return render(request, 'home.html', context)


def post(request, pk):
    post = Post.objects.get(id=pk)
    comments = post.comment_set.all().order_by('-created')

    if request.method == 'POST':
        comment = Comment.objects.create(
            post=post,
            user=request.user,
            body=request.POST.get('body')
        )

    context = {
        'post': post,
        'comments': comments
    }

    return render(request, 'post.html', context)


@login_required(login_url='login')
def createPost(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'create-post.html', context)


@login_required(login_url='login')
def editPost(request, pk):
    post = Post.objects.get(id=pk)
    form = PostForm(instance=post)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'create-post.html', context)


@login_required(login_url='login')
def deletePost(request, pk):
    post = Post.objects.get(id=pk)

    if request.method == 'POST':
        post.delete()
        return redirect('home')

    context = {'obj': post}
    return render(request, 'delete-post.html', context)


@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('login')
