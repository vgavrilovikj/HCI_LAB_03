from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('profile/<str:pk>/', views.profilePage, name='profile'),
    path('profile/<str:pk>/edit', views.editProfile, name='edit-profile'),
    path('post/<str:pk>/', views.post, name='post'),
    path('create-post', views.createPost, name='create-post'),
    path('edit-post/<str:pk>/', views.editPost, name='edit-post'),
    path('delete-post/<str:pk>/', views.deletePost, name='delete-post'),
]
