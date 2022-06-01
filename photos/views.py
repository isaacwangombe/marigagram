from django.shortcuts import render
from django.http  import HttpResponse
from .models import User, Post, Comment, Location, Tag


# Create your views here.
def welcome(request):
  return render(request, 'photos/photos.html')


def post(request):
  post = Post.get_all()
  
  return render(request,'photos/photos.html', {'post' : post})
