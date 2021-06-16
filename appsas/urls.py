from django.urls import path, include
from . import views
from django.urls import reverse_lazy


urlpatterns = [
    path('', views.index, name='index'),
    path('profilis/<int:id>/', views.profilis, name='profilis'),
    path('register/', views.register, name='register'),
    path('profilis/edit/', views.edit_profile, name='edit-profile'),
    path('new_post/', views.new_post, name='new_post'),
    path('search/', views.search, name='search'),
    path('post_detail/<int:post_id>/', views.detailed_post, name='post_detail'),
    path('post/<int:post_id>/remove/', views.post_remove, name='post_remove'),
    path('comment/<int:comment_id>/remove/', views.comment_remove, name='comment_remove'),
    path('like/', views.like_post, name='post_like'),
    # path('<int:post_id>/like/', views.like_post_detailed, name='post_like_detailed'),
]