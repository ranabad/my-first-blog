from django import forms
from django.forms import ModelForm

from .models import (Comment, Education, Experience, Post, Skills,
                     Workshops,Contact)


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
    class Meta:
        model=Contact
        fields=( 'from_email','subject','message')
 
