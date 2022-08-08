from . import views 
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>/', views.PostLike.as_view(), name='post_like'),
    path('delete/<slug:slug>/', views.PostCommentDelete.as_view(), 
         name='delete_post'),
    path('edit/<slug:slug>/', views.PostCommentEdit.as_view(), name='edit_post'),   
]