from django.shortcuts import render
from .models import Post,Shop
from django.contrib import messages

def index(request):
    query=Post.objects.all
    latest = Post.objects.order_by('date')[0:4]
    context={
        'query':query,
        'latest':latest
    }
    return render(request,'index.html',context)



def blog(request):
    recentpost2=Post.objects.order_by('date')[0:3]
    post=Post.objects.all
    post={
        'post':post,
        'recentpost2':recentpost2
    }
    return render(request,'blog.html',post)

def post(request,slug):
    allpost=Post.objects.all
    post=Post.objects.filter(slug=slug)
    recentpost2=Post.objects.order_by('date')[0:3]
    post={
        'post':post,
        'allpost':allpost,
        'recentpost2':recentpost2
    }
    
    return render(request,'post.html',post)

def water(request):
    return render(request,'save_water.html')

def solar_energy(request):
    return render(request,'solar_energy.html')

def plant_important(request):
    return render(request,'plant_important.html')

def recycling_helps(request):
    return render(request,'recycling_helps.html')

def about(request):
    post=Post.objects.all
    recentpost2=Post.objects.order_by('date')[0:3]
   
    post={
        'post':post,
        'recentpost2':recentpost2

        
    }
    return render(request,'about.html',post)

def shop(request):
    shop=Shop.objects.all
    recentpost2=Post.objects.order_by('date')[0:3]
    shop={
        'shop':shop,
        'recentpost2':recentpost2
    }
    return render(request,'shop.html',shop) 


def fitness(request):
    recentpost=Post.objects.order_by('date')[0:4]
    post=Post.objects.all
    recentpost2=Post.objects.order_by('date')[0:3]
    post={
        'post':post,
        'recentpost':recentpost,
        'recentpost2':recentpost2
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
    recentpost=Post.objects.order_by('date')[0:4]
    post=Post.objects.all
    recentpost2=Post.objects.order_by('date')[0:3]
    post={
        'post':post,
        'recentpost':recentpost,
        'recentpost2':recentpost2
    }
    return render(request,'park.html',post) 

def search(request):
    query=request.GET['query']
    recentpost2=Post.objects.order_by('date')[0:3]
    post=Post.objects.filter(desc__icontains=query)
    post=Post.objects.filter(name__icontains=query)
    
    post=Post.objects.filter(title__icontains=query)
    post=Post.objects.filter(slug__icontains=query)

    post={
        'post':post,
        'recentpost2':recentpost2
    }
    return render(request,'search.html',post)

