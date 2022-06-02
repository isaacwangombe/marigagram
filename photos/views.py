from django.shortcuts import redirect, render
from django.http  import HttpResponse
from .models import User, Post, Comment, Location, Tag
from .forms import PostForm
from django.contrib.auth.decorators import login_required




def post(request):
  posts = Post.get_all()
  tags = Tag.get_all_tags()
  
  return render(request,'photos/posts.html', {'posts' : posts, 'tags':tags})



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



@login_required(login_url='/accounts/login/')
def new_post(request):
  current_user = request.user
  if request.method == 'POST':
    form = PostForm(request.POST, request.FILES)
    if form.is_valid():
      upload = form.save(commit=False)
      upload.user = current_user
      upload.save()
    return redirect(post)
  else:
    form=PostForm()

  return render(request, 'photos/new_post.html', {'form': form})

