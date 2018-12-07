from django.shortcuts import render

posts = [
    {
        'author':"Fredrick",
        'title' : "blog post 1",
        'content' : 'First post content',
        'date_posted': 'August 25,2012'
    },
    {
        'author':"dfer",
        'title' : "blog post 2",
        'content' : 'second post content',
        'date_posted': 'August 12,2012'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    #context is a dictionary, key 'posts' will be accessible inside template
    return render(request, 'blog/home.html',context)
# For static html pages 'blog/home.html'
# For dynamic

def about(request):
    return render(request,'blog/about.html',{'title':'About'})
