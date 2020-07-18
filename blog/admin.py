# Register your models here.
from django.contrib import admin

from .models import Post, Comment,Education,Skills,Workshops,Experience

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Education)
admin.site.register(Skills)
admin.site.register(Workshops)
admin.site.register(Experience)
