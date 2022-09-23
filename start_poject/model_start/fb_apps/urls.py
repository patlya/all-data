from .import views
#temprary urls create 
from django.urls import path

urlpatterns = [
    path('<int:us_id>/', views.index),
    path('post/', views.post_detail),
    path('comment/', views.commment_detail),
    path('cmt/', views.cmt_insid_cmt),
    path('followers/', views.followers_detail),
    path('following/', views.following_detail),
    path('like/', views.like_detail),
]