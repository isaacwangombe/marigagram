from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.urls import path


urlpatterns=[
  path('', views.post,name = 'post'),
  path('photo/<id>',views.photo, name='photo' ),
  path('user/<user>', views.search_user,name = 'user'),
  path('post/new/', views.new_post, name='new_post'),
  path('new_comment/<id>',views.new_comment, name='new_comment' ),
  path('profile/<user>',views.profile, name='profile' ),
  path('accounts/register/complete/', views.update_profile, name='update_profile'),



]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


