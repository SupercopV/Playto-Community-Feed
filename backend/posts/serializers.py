from rest_framework import serializers
from .models import Post, Comment

class RecursiveCommentSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    author = serializers.CharField(source="author.username")
    content = serializers.CharField()
    created_at = serializers.DateTimeField()
    children = serializers.SerializerMethodField()

    def get_children(self, obj):
        return RecursiveCommentSerializer(
            obj.children, many=True
        ).data


class PostSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source="author.username")
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ["id", "author", "content", "created_at", "comments"]

    def get_comments(self, obj):
        return RecursiveCommentSerializer(
            obj.comment_tree, many=True
        ).data
