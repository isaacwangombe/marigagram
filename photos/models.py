from django.db import models
from django.contrib.auth.models import User as Editor
from django.db.models import Sum
from cloudinary.models import CloudinaryField



# Create your models here.
class Profile(models.Model):
  profile_image = CloudinaryField('image', null=True, blank=True)
  about = models.TextField(max_length=300, null=True, blank=True)
  user = models.ForeignKey(Editor, on_delete=models.CASCADE, null=True, blank=True )

  def __str__(self):
    return str(self.id)

  def save_profile(self):
    self.save()  	

  def delete_profile(self):
    self.delete()	


  def update_profile(self, new_profile):
      try:
          self.id= new_profile
          self.save()
          return self
      except self.DoesNotExist:
            print('Image you specified does not exist') 

  @classmethod
  def get_all(cls):
        profile = Profile.objects.all()
        return profile		



  @classmethod
  def get_by_id(cls, id):
        profile = cls.objects.filter(id=id).first()	
        return profile

  @classmethod
  def get_by_user(cls, user):
        profile = cls.objects.filter(user=user).first()
        return profile



class Post(models.Model):
  image = CloudinaryField('image', null=True, blank=True)
  image_name = models.CharField(max_length=30)
  caption = models.TextField(max_length=300)
  user = models.ForeignKey(Editor, on_delete=models.CASCADE, )
  profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True  ) 
  post_time = models.DateTimeField(auto_now_add=True)

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
  def get_first(cls):
        post = Post.objects.first()
        return post		



  @classmethod
  def get_by_id(cls, id):
        post = cls.objects.get(id=id)	
        return post

  @classmethod
  def search_by_user(id, search):
        retrieved = id.objects.filter(user__username__icontains=search)
        return retrieved


  @classmethod
  def get_by_user(cls, user):
        profile = cls.objects.filter(user=user).first	
        return profile


class Comment(models.Model):
  comment= models.TextField(max_length=300)
  post_time = models.DateTimeField(auto_now_add=True)
  post = models.ForeignKey(Post, on_delete=models.CASCADE)
  user = models.ForeignKey(Editor, on_delete=models.CASCADE)


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

  
class Vote(models.Model):
  user = models.ForeignKey(Editor, on_delete=models.CASCADE)
  post = models.ForeignKey(Post, on_delete=models.CASCADE)
  vote= models.IntegerField()

  def __str__(self):
    return self.post

  @classmethod
  def get_votes(cls,post):
      retrieved = cls.objects.filter(post=post)
      return retrieved

  @classmethod
  def num_vote(cls):
      found_votes = cls.objects.aggregate(Sum('vote'))
      # found_votes = found_votes.filter(post=post)
      total_votes = sum([i[0] for i in found_votes.all()])

      return total_votes

