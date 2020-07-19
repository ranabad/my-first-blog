# Create your views here.
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from .forms import CommentForm, PostForm , EducationForm,SkillsForm,WorkshopsForm,ExperienceForm,ContactForm
from .models import Comment, Post, Education, Skills,Workshops,Experience,Contact

def CV(request):
  if request.method == 'GET':
        items=Education.objects.all().order_by('-text')
        skills=Skills.objects.all()
        work=Workshops.objects.all()
        exp=Experience.objects.all()
        form1=EducationForm()
        form2=SkillsForm()
        form3=WorkshopsForm()
        form4=ExperienceForm()
        form5 =ContactForm()
  else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['rana.a.albadrani@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
        return redirect('/cv')
 context= {'items': items,'form1': form1,'form2': form2,'skills': skills,'work': work,'form3': form3,'exp': exp,'form4': form4,'form5':form5}
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
def WorkshopsCV(request):
    work = Workshops.objects.all()
    form = WorkshopsForm()
    if request.method == "POST":
        form = WorkshopsForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/cv/Workshop')    
    context={'work': work,'form':form}    
    return render(request, 'blog/cvWorkshop.html', context)
def ExperienceCV(request):
    exp = Experience.objects.all()
    form = ExperienceForm()
    if request.method == "POST":
        form = ExperienceForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/cv/Experience')    
    context={'exp': exp,'form':form}    
    return render(request, 'blog/cvExperience.html', context)    
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
def WorkshopsCVUpdatde(request, pk):
    work = Workshops.objects.get(pk=pk)
    
    form = WorkshopsForm(instance=work)
    if request.method == "POST":
        form = WorkshopsForm(request.POST, instance=work)
        if form.is_valid():
            form.save()
        return redirect('/cv/Workshop')    
    context={'form':form}
    return render(request, 'blog/cvWorkshpsUpdate.html', context)  
@login_required    
def WorkshopsCVDlt(request, pk):
    work = Workshops.objects.get(pk=pk) 
    if request.method == "POST":
        work.delete()
        return redirect('/cv/Workshop')     
    context={'work':work}
    return render(request, 'blog/cvWorkshopDlt.html', context)
@login_required    
def ExperienceCVUpdatde(request, pk):
    exp = Experience.objects.get(pk=pk)
    
    form = ExperienceForm(instance=exp)
    if request.method == "POST":
        form = ExperienceForm(request.POST, instance=exp)
        if form.is_valid():
            form.save()
        return redirect('/cv/Experience')    
    context={'form':form}
    return render(request, 'blog/cvExperienceUpdate.html', context)  
@login_required    
def ExperienceCVDlt(request, pk):
    exp = Experience.objects.get(pk=pk) 
    if request.method == "POST":
        exp.delete()
        return redirect('/cv/Experience')     
    context={'exp':exp}
    return render(request, 'blog/cvExperienceDlt.html', context) 

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
