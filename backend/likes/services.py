from django.db import transaction, IntegrityError
from .models import PostLike, CommentLike
from karma.models import KarmaTransaction

def like_post(user, post):
    """
    Atomically like a post and give karma to the post author.
    """
    try:
        with transaction.atomic():
            PostLike.objects.create(user=user, post=post)
            KarmaTransaction.objects.create(
                user=post.author,
                source_type=KarmaTransaction.POST_LIKE,
                source_id=post.id,
                points=5
            )
        return True
    except IntegrityError:
        return False


def like_comment(user, comment):
    """
    Atomically like a comment and give karma to the comment author.
    """
    try:
        with transaction.atomic():
            CommentLike.objects.create(user=user, comment=comment)
            KarmaTransaction.objects.create(
                user=comment.author,
                source_type=KarmaTransaction.COMMENT_LIKE,
                source_id=comment.id,
                points=1
            )
        return True
    except IntegrityError:
        return False
