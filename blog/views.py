from django.shortcuts import render

from .forms import BlogPostForm


def index(request):
    return render(request, 'blog/index.html')


def post_new(request):
    form = BlogPostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
