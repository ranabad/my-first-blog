from django import forms
from django.forms import ModelForm

from .models import Comment, Post ,Item


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)        
class CVForm(forms.ModelForm):
        class Meta:
            model=Item
            fields='__all__'


