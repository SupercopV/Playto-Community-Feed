from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer
from .services import build_comment_tree

class FeedView(APIView):
    def get(self, request):
        posts = Post.objects.select_related("author").all()

        response = []
        for post in posts:
            post.comment_tree = build_comment_tree(post.id)
            response.append(PostSerializer(post).data)

        return Response(response)


# Create your views here.
