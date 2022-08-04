from . import views 
# from .views import PostEdit
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name = 'home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name = 'post_detail'),
    path('like/<slug:slug>/', views.PostLike.as_view(), name = 'post_like'),
    path('comment/<slug:slug>/update', UpdatePostView.as_view(), name ='update_post'),
]