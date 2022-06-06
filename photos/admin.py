from django.contrib import admin
from django.contrib import admin
from .models import Profile, Post, Comment, Location, Tag


# Register your models here.

class PostAdmin(admin.ModelAdmin):
  filter_horizontal =('location','tag')

admin.site.register(Profile)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Location)
admin.site.register(Tag)