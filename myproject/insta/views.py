from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post
from django.contrib.auth.decorators import login_required

@login_required
def addpost(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('feed')
    else:
        form = PostForm()

   
    return render(request, "insta/addpost.html", {"form": form})

def success(request):
    return render(request, "insta/success.html")

def view_posts(request):
    # Show only public posts to everyone
    posts = Post.objects.filter(is_public=True).order_by('-created_at')
    return render(request, "insta/feed.html", {"posts": posts})

def feed(request):
    posts = Post.objects.filter(is_public=True).order_by('-created_at')
    return render(request, 'insta/feed.html', {'posts': posts})