from django.urls import path
from . import views

urlpatterns = [
    path('', views.Registration.as_view(), name='registration'),
    path('signin', views.SignIn.as_view(), name='signin'),
    path('feed', views.PostsFeed.as_view(), name='feed'),
    path('create_post', views.CreatePost.as_view(), name='create_post'),
    path('edit_post/<int:post_id>', views.EditPost.as_view(), name='edit_post'),
    path('logout', views.logout_user, name='logout'),
]
