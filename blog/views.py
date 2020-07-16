# Create your views here.
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from .forms import CommentForm, PostForm , EducationForm,SkillsForm
from .models import Comment, Post, Education, Skills

def CV(request):
    items=Education.objects.all()
    skills=Skills.objects.all()
    form1=EducationForm()
    form2=SkillsForm()
    
    context= {'items': items,'form1': form1,'form2': form2,'skills': skills}
    return render(request, 'blog/cv.html', context)
def EducationCV(request):
    items = Education.objects.all()
    form = EducationForm()
    if request.method == "POST":
        form = EducationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/cv/Education')    
    context={'items': items,'form':form}
    return render(request, 'blog/cvEducation.html', context)
def SkillsCV(request):
    skills = Skills.objects.all()
    form = SkillsForm()
    if request.method == "POST":
        form = SkillsForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/cv/Skills')    
    context={'skills': skills,'form':form}
    return render(request, 'blog/cvSkills.html', context)              
@login_required    
def EducationCVUpdatde(request, pk):
    items = Education.objects.get(pk=pk)
    
    form = EducationForm(instance=items)
    if request.method == "POST":
        form = EducationForm(request.POST, instance=items)
        if form.is_valid():
            form.save()
        return redirect('/cv/Education')    
    context={'form':form}
    return render(request, 'blog/cvEducationUpdate.html', context)  
@login_required    
def EducationCVDlt(request, pk):
    items = Education.objects.get(pk=pk) 
    if request.method == "POST":
        items.delete()
        return redirect('/cv/Education')     
    context={'items':items}
    return render(request, 'blog/cvEducationDlt.html', context)
@login_required    
def SkillsCVUpdatde(request, pk):
    skills = Skills.objects.get(pk=pk)
    form = SkillsForm(instance=skills)
    if request.method == "POST":
        form = SkillsForm(request.POST, instance=skills)
        if form.is_valid():
            form.save()
        return redirect('/cv/Skills')    
    context={'form':form}
    return render(request, 'blog/cvSkillsUpdate.html', context)  
@login_required    
def SkillsCVDlt(request, pk):
    skills = Skills.objects.get(pk=pk) 
    if request.method == "POST":
        skills.delete()
        return redirect('/cv/Skills')     
    context={'skills':skills}
    return render(request, 'blog/cvSkillsDlt.html', context)            
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
@login_required    
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})    
@login_required    
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)
@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')

def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})
@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)
