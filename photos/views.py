from django.shortcuts import render
from django.http  import HttpResponse
from .models import User, Post, Comment, Location, Tag


def post(request):
  post = Post.get_all()
  tag = Tag.get_all_tags()
  
  return render(request,'photos/posts.html', {'post' : post, 'tag':tag})



def photo(request):
  post = Post.get_by_id(id)

  return render(request, 'photos/photo.html', {'post':post, 'id':id})

def search_user(request):
  if 'user' in request.GET and request.GET['user']:
    search_term = request.GET.get('user')
    user = Post.search_by_user(search_term)
    message = f'{search_term}'

    return render(request, 'photos/user.html', {'message':message, 'user':user})
		# if it is a search bar:
  else :
    message = 'We have not found your search term'
    return render(request, 'photos/user.html', {'message':message})



def search_tag(request):
		search_term = request.GET.get('tag')
		name = Post.search_by_tag(search_term)
		message = f'{search_term}'

		return render(request, 'photos/tag.html', {'message':message, 'name':name})