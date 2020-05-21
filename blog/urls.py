from django.urls import path
from . import views
from .views import (PostListView,PostDetailView,PostCreateView)

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('<int:pk>/', PostDetailView.as_view(), name='blog-details'),
    path('new/', PostCreateView.as_view(), name='post-create'),
    path('about/',views.about, name='blog-about'),
]