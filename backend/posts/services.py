from .models import Comment

def build_comment_tree(post_id):
    """
    Fetch all comments for a post in ONE query
    and build a nested tree in memory.
    """
    comments = (
        Comment.objects
        .filter(post_id=post_id)
        .select_related("author")
        .order_by("created_at")
    )

    comment_map = {}
    roots = []

    for comment in comments:
        comment.children = []
        comment_map[comment.id] = comment

    for comment in comments:
        if comment.parent_id:
            parent = comment_map.get(comment.parent_id)
            if parent:
                parent.children.append(comment)
        else:
            roots.append(comment)

    return roots
