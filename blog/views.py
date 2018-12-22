from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from django.urls import reverse
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request,title):
    post = get_object_or_404(Post,title=title, available=True)
    context = {
        'post': post,
    }
    return render(request, 'blog/post_detail.html', context)