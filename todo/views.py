from django.shortcuts import render,redirect
from .models import todo
# Create your views here.


def add(request):
    all=todo.objects.all()
    if(request.method=='POST'):
        title=request.POST['title']
        todo.objects.create(title=title)
        return redirect('add')

    return render(request,'index.html',{"all":all})


def delete(request,id):
    todo.objects.get(pk=id).delete()
    return redirect('add')


def update(request,id):
    post=todo.objects.get(pk=id)
    if(request.method=='POST'):
        title=request.POST['title']
        post.title=title
        post.save()
        return redirect('add')
    else:
        return render(request,'index.html',{"all":all,'post':post})