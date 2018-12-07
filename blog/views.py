from django.shortcuts import render
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    #context is a dictionary, key 'posts' will be accessible inside template
    return render(request, 'blog/home.html',context)
# For static html pages 'blog/home.html'
# For dynamic

def about(request):
    return render(request,'blog/about.html',{'title':'About'})
