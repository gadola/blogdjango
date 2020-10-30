from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter




urlpatterns = [
    path('', views.PostListView.as_view(), name="index"),
    # path('', views.Index.as_view(), name="index"),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name="post_detail"),
    path('add_post/', views.add_post, name="add_post"),
    path('update/<int:pk>/', views.PostUpdate.as_view(), name="update_post"),
    path('delete/<int:pk>/', views.deletePost, name="delete_post"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('search/', views.search, name="search"),
    # path('api/', views.PostList.as_view(), name="api_list"),
    # path('api/post/<int:pk>/', views.PostDetail.as_view(), name="api_ud"),

]