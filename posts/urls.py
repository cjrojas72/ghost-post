from django.urls import path
from posts import views

urlpatterns = [
    path('', views.Index, name='home'),
    path('addpost/', views.AddPost)
]
