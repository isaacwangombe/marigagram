from django.db import models

# Create your models here.
class User(models.Model):
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  user_name = models.CharField(max_length=30)
  password = models.CharField(max_length=30)
  email = models.EmailField()

  def __str__(self):
    return self.user_name

  def save_user(self):
    self.save()  	

  def delete_user(self):
    self.delete()	


  def update_user(self, new_user):
      try:
          self.user_name= new_user
          self.save()
          return self
      except self.DoesNotExist:
            print('Image you specified does not exist') 


class Location(models.Model):
  location = models.CharField(max_length=30)

  def __str__(self):
      return self.location

  def save_location(self):
    self.save()  	

  def delete_location(self):
    self.delete()	


  def update_location(self, new_location):
      try:
          self.id = new_location
          self.save()
          return self
      except self.DoesNotExist:
            print('Image you specified does not exist') 

class Tag(models.Model):
  tag = models.CharField(max_length=30)

  def __str__(self):
      return self.tag

  def save_tag(self):
    self.save()  	

  def delete_tag(self):
    self.delete()	


  def update_tag(self, new_tag):
      try:
          self.id = new_tag
          self.save()
          return self
      except self.DoesNotExist:
            print('Image you specified does not exist') 

  @classmethod
  def get_all_tags(cls):
        tag = Tag.objects.all()
        return tag	



class Post(models.Model):
  image = models.ImageField(upload_to='posts/')
  image_name = models.CharField(max_length=30)
  caption = models.TextField(max_length=300)
  user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
  post_time = models.DateTimeField(auto_now_add=True)
  location = models.ManyToManyField(Location)
  tag = models.ManyToManyField(Tag)

  def __str__(self):
    return str(self.id)

  def save_post(self):
    self.save()  	

  def delete_post(self):
    self.delete()	


  def update_post(self, new_post):
      try:
          self.id = new_post
          self.save()
          return self
      except self.DoesNotExist:
            print('Image you specified does not exist') 

	
  @classmethod
  def get_all(cls):
        post = Post.objects.all()
        return post		



  @classmethod
  def get_by_id(cls, id):
        post = cls.objects.get(id=id)	
        return post

  @classmethod
  def search_by_user(id, user):
        retrieved = id.objects.filter(user__user_name__contains=user)
        return retrieved

  @classmethod
  def search_by_tag(id, tag):
        retrieved = id.objects.filter(user__user_name__contains=tag)
        return retrieved




class Comment(models.Model):
  comment= models.TextField(max_length=300)
  post_time = models.DateTimeField(auto_now_add=True)
  user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
  post = models.ForeignKey(Post, on_delete=models.DO_NOTHING)

  def __str__(self):
    return self.comment

  def save_comment(self):
    self.save()  	

  def delete_comment(self):
    self.delete()	


  def update_comment(self, new_comment):
      try:
          self.id = new_comment
          self.save()
          return self
      except self.DoesNotExist:
            print('Comment you specified does not exist') 
