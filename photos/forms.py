import imp
from .models import Post, Comment


class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    exclude = ['user', 'post_time']
