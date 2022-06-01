from django.shortcuts import render
from django.http  import HttpResponse
from .models import User, Post, Comment, Location, Tag


def post(request):
  post = Post.get_all()
  
  return render(request,'photos/posts.html', {'post' : post})



def photo(request):
  post = Post.get_by_id(id)

  return render(request, 'photos/photo.html', {'post':post, 'id':id})


