from django.urls import path, include
from . import views
from django.urls import reverse_lazy


urlpatterns = [
    path('', views.index, name='index'),
    path('profilis/<int:id>/', views.profilis, name='profilis'),
    path('register/', views.register, name='register'),
    path('profilis/edit/', views.edit_profile, name='edit-profile'),
    path('new_post/', views.new_post, name='new_post'),
    # path('search/', views.search, name='search'),
    # path('profilis/<int:id>/', views.other_profile, name='other_profile'),
    # path('post_detail/<str:username>/<int:pk>', views.DetailedPostView.as_view(), name='detail-view'),
]