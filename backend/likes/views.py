from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from posts.models import Post, Comment
from .services import like_post, like_comment

class PostLikeView(APIView):
    def post(self, request, post_id):
        user = request.user
        post = get_object_or_404(Post, id=post_id)

        success = like_post(user, post)
        if success:
            return Response({"message": "Post liked"}, status=status.HTTP_201_CREATED)
        return Response({"message": "Already liked"}, status=status.HTTP_200_OK)


class CommentLikeView(APIView):
    def post(self, request, comment_id):
        user = request.user
        comment = get_object_or_404(Comment, id=comment_id)

        success = like_comment(user, comment)
        if success:
            return Response({"message": "Comment liked"}, status=status.HTTP_201_CREATED)
        return Response({"message": "Already liked"}, status=status.HTTP_200_OK)

# Create your views here.
