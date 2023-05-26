from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm

from blog.forms import PostForm, CategoryForm
from blog.models import Post, Category


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user=user)
            return redirect('home')
        else:
            error_message = 'Invalid username or password.'
            return render(request, 'login.html', {'error_message': error_message})
    return render(request, 'login.html')


def home(request):
    category = request.GET.get('category')
    query = request.GET.get('q')
    posts = Post.objects.filter(user=request.user.id).order_by('category')
    if category:
        posts = posts.filter(category=category)
    if query:
        posts = posts.filter(Q(title__icontains=query) | Q(content__icontains=query))
    categories = Category.objects.all()
    return render(request, 'home.html',
                  {'posts': posts, 'category': category, 'query': query, 'categories': categories})


@login_required
def create_post(request):
    # import ipdb;
    # ipdb.set_trace()
    if request.method == 'POST':
        form = PostForm(request.POST)
        category_form = CategoryForm(request.POST)  # New category form
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            category_id = request.POST.get('category')

            if not category_id:
                # No category selected, create a new one
                category = category_form.save()
            else:
                category = Category.objects.get(id=category_id)
            post.category = category  # Associate the post with the category
            post.save()
            return redirect('home')
    else:
        form = PostForm()
        category_form = CategoryForm()  # Empty category form

    return render(request, 'create_post.html', {'form': form, 'category_form': category_form})


@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, user=request.user.id)
    if request.method == 'POST':
        post.delete()
        return redirect('home')

    return render(request, 'delete_post.html', {'post': post})


@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, user=request.user.id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm(instance=post)
    return render(request, 'edit_post.html', {'form': form})


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id, user=request.user.id)
    return render(request, 'post_detail.html', {'post': post})


@login_required
def create_category(request):
    if request.method == 'POST':
        category_name = request.POST.get('category_name')
        category = Category.objects.create(name=category_name)
        return redirect('blog:create_post')

    return render(request, 'create_category.html')
