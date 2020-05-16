from django.urls import path
from posts import views

urlpatterns = [
    path('', views.Index, name='home'),
    path('addpost/', views.AddPost),
    path('like/<int:id>/', views.LikeView),
    path('dislike/<int:id>', views.DislikeView),
    path('choice/<str:choices>', views.FilterView)
]
