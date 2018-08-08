from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth import authenticate, get_user_model, login, logout
from blog.models import Post
from pages.forms import PostForm
from pages.forms import UserLoginForm

# Create your views here.

def home_view(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
	paginator = Paginator(posts, 5) # Число дописів на сторінці
	page = request.GET.get('page')
	posts = paginator.get_page(page)
	return render(request, 'home.html', {'posts': posts})

def post_detail_view(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'post_detail.html', {'post': post})

def new_post_view(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'post_edit.html', {'form': form})

def post_edit_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'post_edit.html', {'form': form})


def contact_view(request, *args, **kwargs):
	return render(request, "contacts.html", {})

def information_view(request, *args, **kwargs):
	return render(request, "information.html", {})

def regulations_view(request, *args, **kwargs):
	return render(request, "regulations.html", {})

def login_view(request, *args, **kwargs):
    # print(request.user.is_authenticated())
    title = "Вхід"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        # print(request.user.is_authenticated())
    return render(request, "login.html", {"form": form, "title": title})

def logout_view(request, *args, **kwargs):
    logout(request)
    return render(request, "login.html", {})

def registration_view(request, *args, **kwargs):
    return render(request, "login.html", {})

def dashboard_view(request, *args, **kwargs):
    return render(request, "dashboard.html", {})