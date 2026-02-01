from django.db import models
from django.contrib.auth.models import User
from posts.models import Post, Comment


class KarmaTransaction(models.Model):
    POST_LIKE = "POST"
    COMMENT_LIKE = "COMMENT"

    SOURCE_CHOICES = [
        (POST_LIKE, "Post Like"),
        (COMMENT_LIKE, "Comment Like"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    source_type = models.CharField(max_length=10, choices=SOURCE_CHOICES)
    source_id = models.PositiveIntegerField()
    points = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} +{self.points}"

