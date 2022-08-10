from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>/', views.PostLike.as_view(), name='post_like'),
    path('user_comments/delete-comment/<int:pk>/',
         views.PostCommentDelete.as_view(),
         name='delete-comment'),
    path('user_comments/edit-comment/<int:pk>/',
         views.PostCommentEdit.as_view(),
         name='edit-comment')
]
