from django.urls import path
from . import views
from .views import (PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView)

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('<int:pk>/', PostDetailView.as_view(), name='blog-details'),
    path('new/', PostCreateView.as_view(), name='post-create'),
    path('<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/',views.about, name='blog-about'),
]