from django.shortcuts import render
from .models import Post

def home(request):
    posts = Post.objects.all()
    context = {
        'site_name':'My Blog App',
        'posts': posts
    }
    return render(request,'home.html',context)


def about(request):
    context = {
        'title':'About Page',
    }
    return render(request,'about.html',context)    


def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {
        'post': post   
    }
    return render(request,'post_details.html',context)

def user_posts(request, username):
    
    post = Post.objects.filter(author__username=username)

    context = {
        'posts': post,
        'username': username,
    }

    return render(request, 'user_posts.html', context)
