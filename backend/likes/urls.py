from django.urls import path
from .views import PostLikeView, CommentLikeView

urlpatterns = [
    path("posts/<int:post_id>/like/", PostLikeView.as_view()),
    path("comments/<int:comment_id>/like/", CommentLikeView.as_view()),
]
