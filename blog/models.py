# Create your models here.
from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
#from django.utils.translation import as_, ugettext_lazy


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

@python_2_unicode_compatible
class CV(models.Model):
    first_name=models.CharField(_("First name")), max_length=40)
    last_name=models.CharField(_("First name")), max_length=40)
    email=models.EmailField(_("Email"))

    def __str__(self):
        return self.first_name+" "+self.last_name
@python_2_unicode_compatible
class Experince(models.Model):
    cv=models.ForeignKey(CV)
    from_date=models.DateField(_("From"))
    till_date=models.DateField(_("Till")),null=True, blank=True)
    company=models.CharField(_("Company")),max_length=100)
    company=models.CharField(_("Position")),max_length=100)
    skills= models.TextField(_("Skills gained")), blank=True)

    def __str__(self):
        till=_("present")
        if self.till_date:
            till=self.till_date.strftime("%m/%Y")
        return _("%(from)s-%(till)s%(pos)s at %(company)s")%{
            "from":self.from_date.strftime("%m/%Y"),
            "till":till,
            "pos":self.position,
            "company":self.company,
        }   
class Meta:
    ordering=("- from_date",)
