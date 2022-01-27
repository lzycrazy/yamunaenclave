from django.shortcuts import render
from .models import Post,Shop
from django.contrib import messages

def index(request):
    # allpost=Post.objects.all
    post=Post.objects.all
    recentpost=Post.objects.order_by('-slug')[0:4]
    recentpost2=Post.objects.order_by('date')[0:3]
    context={
        'post':post,
        'recentpost':recentpost,
        'recentpost2':recentpost2

    }
    return render(request,'index.html',context)


def blog(request):
    post=Post.objects.all
    recentpost2=Post.objects.order_by('date')[0:3]
    post={
        'post':post,
        'recentpost2':recentpost2,
    }
    return render(request,'blog.html',post)

def post(request,slug):
    allpost=Post.objects.all
    post=Post.objects.filter(slug=slug)
    recentpost2=Post.objects.order_by('date')[0:3]
    
    post={
        'post':post,
        'allpost':allpost,
        'recentpost2':recentpost2,
    }
    
    return render(request,'post.html',post)

def about(request):
    post=Post.objects.all
    recentpost=Post.objects.order_by('date')[0:4]
    recentpost2=Post.objects.order_by('date')[0:3]
   
    post={
        'post':post,
        'recentpost':recentpost,
        'recentpost2':recentpost2
        
    }
    return render(request,'about.html',post)

def shop(request):
    recentpost2=Post.objects.order_by('date')[0:3]
    shop=Shop.objects.all

    shop={
        'shop':shop,
        'recentpost2':recentpost2
    }
    return render(request,'shop.html',shop) 


def fitness(request):
    post=Post.objects.all
    recentpost=Post.objects.order_by('date')[0:4]
    recentpost2=Post.objects.order_by('date')[0:3]
   
    post={
        'post':post,
        'recentpost2':recentpost2,
        'recentpost':recentpost,
        
    }
    return render(request,'fitness.html',post)

def productview(request,slug):
    shop=Shop.objects.filter(slug=slug)
    recentpost2=Post.objects.order_by('date')[0:3]
    shop={
        'shop':shop,
        'recentpost2':recentpost2
    }
    return render(request,'productview.html',shop)  

def park(request):
    post=Post.objects.all
    recentpost=Post.objects.order_by('date')[0:4]
    recentpost2=Post.objects.order_by('date')[0:3]
    post={
        'post':post,
        'recentpost2':recentpost2,
        'recentpost':recentpost,
        
        
    }
    return render(request,'park.html',post) 

def search(request):
    recentpost2=Post.objects.order_by('date')[0:3]
    query=request.GET['query']
   
    post=Post.objects.filter(desc__icontains=query)
    post=Post.objects.filter(name__icontains=query)
    
    post=Post.objects.filter(title__icontains=query)
    post=Post.objects.filter(slug__icontains=query)

    post={
        'post':post,
        'recentpost2':recentpost2
        
    }
    return render(request,'search.html',post)

