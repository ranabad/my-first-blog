from django import forms
from django.forms import ModelForm

from .models import Comment, Post ,Education, Skills


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
            fields=( 'text','date','grade')
class SkillsForm(forms.ModelForm):
        class Meta:
            model=Skills
            fields=( 'text',)






