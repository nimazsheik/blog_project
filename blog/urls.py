from django.urls import path
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView
)

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('about/',views.about, name='blog-about'),
    # pk  is primary key of post,only allowing integers with int
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),  # post_detail
    path('post/new/', PostCreateView.as_view(), name='post-create'),  # this naming is post_form <model_form>

]