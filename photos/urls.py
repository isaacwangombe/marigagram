from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.urls import path


urlpatterns=[
  path('', views.post,name = 'post'),
  path('photo/<id>',views.photo, name='photo' ),
  path('user/', views.search_user,name = 'user'),
  path('tag/', views.search_tag,name = 'user'),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


