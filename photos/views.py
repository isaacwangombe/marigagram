from django.shortcuts import redirect, render
from django.http  import HttpResponse
from .models import Profile, Post, Comment
from .forms import PostForm, CommentForm, ProfileForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User as Editor




def post(request):
  posts = Post.get_all()
  profile = Profile.get_all()
  
  
  return render(request,'photos/posts.html', {'posts' : posts, 'profile':profile})



def photo(request, id):
  post = Post.get_by_id(id)

  return render(request, 'photos/photo.html', {'post':post, 'id':id})



def search_user(request):
    if 'user' in request.GET and request.GET['user']:
        search = request.GET.get('user')
        posts = Post.search_by_user(search)
        

        message = f'{search}'

        return render(request, 'photos/user.html', {'message':message, 'posts':posts})
    else:
        message = 'You have not searched any term'
        return render(request, 'photos/user.html', {'message':message})



@login_required(login_url='/accounts/login/')
def new_post(request):
  current_user = request.user
  if request.method == 'POST':
    form = PostForm(request.POST, request.FILES)
    if form.is_valid():
      upload = form.save(commit=False)
      upload.user = current_user
      upload.save()
    return redirect('post')
  else:
    form=PostForm()

  return render(request, 'photos/new_post.html', {'form': form})




@login_required(login_url='/accounts/login/')
def new_comment(request, id):
  current_user = request.user
  post = Post.get_by_id(id)
  if request.method == 'POST':
    form = CommentForm(request.POST)
    if form.is_valid():
      comment = form.save(commit=False)
      comment.user = current_user
      comment.post = post
      comment.save()
    return redirect('post')
  else:
    form=CommentForm()

  return render(request, 'photos/new_comment.html', {'form': form, 'id':id, "post":post})



def profile(request, user):
  profile = Profile.get_by_user(user)
  post = Post.get_by_user(user)
  posts = Post.search_by_user(user)

  return render(request,'registration/profile.html', {'profile' : profile,  'post':post, 'user':user, 'posts':posts})




@login_required(login_url='/accounts/login/')
def update_profile(request):
  current_user = request.user
  if request.method == 'POST':
    form = ProfileForm(request.POST, request.FILES)
    if form.is_valid():
      profile = form.save(commit=False)
      profile.user = current_user
      profile.save()
    return redirect('post')
  else:
    form=ProfileForm()

  return render(request, 'django_registration/registration_complete.html', {'form': form})

