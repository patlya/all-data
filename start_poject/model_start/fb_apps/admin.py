from django.contrib import admin



#admin_name:-admin2
#admin_password:-admin1234
# Register your models here.
from .models import *

@admin.register(ExtendedUser)
class ExtendedUserAdmin(admin.ModelAdmin):
    list_display=['user','user_contact','gender','education','user_address']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=['content','post_date','content_description']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display=['comment']


@admin.register(Comment_inside_cmt)
class Comment_inside_cmtAdmin(admin.ModelAdmin):
    list_display=['comment_reply']

admin.site.register(NewFollowers)
admin.site.register(NewFollowing)    
admin.site.register(Like)   

      