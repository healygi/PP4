from . import views 
from django.urls import path
# from .views import PostCommentEdit

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>/', views.PostLike.as_view(), name='post_like'),
    # path('delete/<slug:slug>/', views.PostCommentDelete.as_view(), 
    #      name='delete_post'),
    # path('update/<slug:slug>/', PostCommentEdit.as_view(), name='edit_post'),   
]