# Register your models here.
from django.contrib import admin

from .models import Post, Comment,Education,Skills

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Education)
admin.site.register(Skills)
