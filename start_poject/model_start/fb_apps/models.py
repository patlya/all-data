from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class ExtendedUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_contact=models.CharField(max_length=15, null=True, blank=True)
    user_address=models.TextField(max_length=200)
    gender=models.CharField(max_length=100,null=True,blank=True)
    education=models.TextField(max_length=200,null=True,blank=True)
    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            ExtendedUser.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.extendeduser.save()

    def __str__(self):
        return self.user.username

class Post(models.Model):
    
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    content=models.CharField(max_length=200,null=True,blank=True)
    post_date=models.DateField()
    content_description=models.TextField(max_length=200,null=True,blank=True)

    def __str__(self):
        return self.content

class Comment(models.Model):
   
    comment=models.CharField(max_length=90,null=True,blank=True)  #Comment.objects.all().first().post_id.user_id.username
    post_id=models.ForeignKey(Post,on_delete=models.CASCADE)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.comment

class Comment_inside_cmt(models.Model):
    coment_id= models.ForeignKey(Comment,on_delete=models.CASCADE)
    user_id= models.ForeignKey(User,on_delete=models.CASCADE)  
    comment_reply=models.CharField(max_length=90,null=True,blank=True) 

    def __str__(self):
        return self.comment_reply


class NewFollowers(models.Model):
    usr_follrs=models.OneToOneField(User,on_delete=models.CASCADE,related_name="usr_follrs",null=True,blank=True)
    follow_user_id=models.ManyToManyField(User, blank=True,null=True,related_name='follower') 

class NewFollowing(models.Model):
    usr_follwing=models.OneToOneField(User,on_delete=models.CASCADE,related_name="user_following",null=True,blank=True)
    following_user_name=models.ManyToManyField(User,blank=True,null=True,related_name='following')

# class UserFollowers(models.Model):
#     usr_follrs=models.OneToOneField(User,on_delete=models.CASCADE,related_name="usr_follrs",null=True,blank=True)
#     follow_user_id=models.ManyToManyField(User, blank=True,null=True,related_name='follower') 

# class UserFollowing(models.Model):
#     usr_follwing=models.OneToOneField(User,on_delete=models.CASCADE,related_name="user_following",null=True,blank=True)
#     following_user_name=models.ManyToManyField(User,blank=True,null=True,related_name='following')


class Like(models.Model):
    post_id=models.ForeignKey(Post,on_delete=models.CASCADE)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)    