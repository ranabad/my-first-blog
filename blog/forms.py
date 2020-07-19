from django import forms
from django.forms import ModelForm

from .models import (Comment, Contact, Education, Experience, Post, Skills,
                     Workshops)


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)        
class EducationForm(forms.ModelForm):
        class Meta:
            model=Education
            fields=( 'text','date',)
class SkillsForm(forms.ModelForm):
        class Meta:
            model=Skills
            fields=( 'text',)
class WorkshopsForm(forms.ModelForm):
        class Meta:
            model=Workshops
            fields=( 'text','date',) 
class ExperienceForm(forms.ModelForm):
        class Meta:
            model=Experience
            fields=( 'text','date',)
class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
