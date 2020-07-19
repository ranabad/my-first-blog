# Create your models here.

from django.conf import settings
from django.db import models
from django.utils import timezone
import datetime





class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return self.title
    def approved_comments(self):
        return self.comments.filter(approved_comment=True)    

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

class Education(models.Model):
    text = models.CharField(max_length=200)
    date = models.CharField(max_length=200 ,default='Present')
    grade =models.CharField(max_length=200,default='Not applicable')
    def __str__(self):
        temp = '{text} {date} {grade}'
        return temp.format(self)
    
class Skills(models.Model):
    text = models.CharField(max_length=200)   
    def __str__(self):
        return self.text     
class Workshops(models.Model):
    text = models.CharField(max_length=200)
    date = models.CharField(max_length=200 ,default='Present')
    def __str__(self):
        template = '{text} {date}'
        return template.format(self)
class Experience(models.Model):
    text = models.CharField(max_length=200)
    date = models.CharField(max_length=200 ,default='Present')
    def __str__(self):
        exp = '{text} {date}'
        return exp.format(self)
class Contact(models.Model):
    from_name =models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.CharField(max_length=200)
    def __str__(self):
        con = '{from_email} {subject} {message}'
        return con.format(self)         



   