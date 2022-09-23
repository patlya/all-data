from django.http import HttpResponse
from django.shortcuts import render
from .models import *
# Create your views here.
def index(request,us_id):
    obj_list=ExtendedUser.objects.all()#.values()
    return render(request,'fb_app/index.html',{'obj_list':obj_list})
    return HttpResponse(obj_list,us_id)
    

def post_detail(request):
    post_values=Post.objects.all()
    # return HttpResponse(post_values) 
    # import pdb;pdb.set_trace() 
    return render(request,'fb_app/index.html',{'post_values':post_values}) 

def commment_detail(request):
    comment_values=Comment.objects.all()
    
    return render(request,'fb_app/index.html',{'comment_values':comment_values})   

def cmt_insid_cmt(request):
    cmt_values=Comment_inside_cmt.objects.all()
    return render(request,'fb_app/index.html',{'cmt_values':cmt_values}) 

def followers_detail(request):
    follo_values=NewFollowers.objects.all()
     
    return render(request,'fb_app/index.html',{'follo_values':follo_values}) 

def following_detail(request):
    flwing_values=NewFollowing.objects.all().values()
    
    return render(request,'fb_app/index.html',{' flwing_values':flwing_values})   


def like_detail(request):
    like_values=Like.objects.all().values()
    return render(request,'fb_app/index.html',{' flwing_values':like_values})                         
