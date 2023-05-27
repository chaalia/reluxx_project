from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = 'blog'
urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.user_login, name='login'),
    path('create/', views.create_post, name='create_post'),
    path('view/<int:post_id>/', views.post_detail, name='view_post'),
    path('delete/<int:post_id>/', views.delete_post, name='delete_post'),
    path('edit/<int:post_id>/', views.edit_post, name='edit_post'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('create_categ/', views.create_category, name='create_category'),
]
