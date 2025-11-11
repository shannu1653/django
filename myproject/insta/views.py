from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import PostForm
from .models import Post

def feed(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'insta/feed.html', {'posts': posts})

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "🎉 Post uploaded successfully!")
            return redirect('feed')
    else:
        form = PostForm()
    return render(request, 'insta/create_post.html', {'form': form})
