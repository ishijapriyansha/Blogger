from django.shortcuts import render, redirect, get_object_or_404
from home.models import Blog
from home.db import db  

def index(request):
    if request.method == "POST":
        title = request.POST.get('title')
        desc = request.POST.get('desc')

        if title and desc:  
            blog = Blog.objects.create(title=title, desc=desc)
            db.insert_one({'_id': blog.id, 'title': blog.title, 'desc': blog.desc})

    blogs = Blog.objects.all()
    return render(request, 'index.html', {'blogs': blogs})

def update_blog(request, id):
    blog = get_object_or_404(Blog, id=id)

    if request.method == "POST":
        blog.title = request.POST.get('title')
        blog.desc = request.POST.get('desc')
        blog.save()

        db.update_one({'_id': blog.id}, {'$set': {'title': blog.title, 'desc': blog.desc}})
        return redirect('home') 

    return render(request, 'update_blog.html', {'blog': blog})

def delete_blog(request, id):
    blog = get_object_or_404(Blog, id=id)
    db.delete_one({'_id': blog.id})  
    blog.delete()
    return redirect('home')
