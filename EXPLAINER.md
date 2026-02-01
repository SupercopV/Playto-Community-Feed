#1. The Tree — Nested Comments Design
How comments are modeled

Nested comments are modeled using a self-referential foreign key.

Each comment has:

a post it belongs to

an optional parent comment (nullable)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    parent = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        related_name="replies",
        on_delete=models.CASCADE
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


This allows:

Top-level comments → parent = NULL

Replies → parent = <another comment>

How the tree is fetched efficiently (avoiding N+1)

Instead of recursively querying the database, all comments for a post are fetched in a single query, then assembled into a tree in memory.

comments = Comment.objects.filter(post_id=post_id).select_related("author")


A service-layer function builds the tree:

def build_comment_tree(post_id):
    comments = Comment.objects.filter(post_id=post_id).select_related("author")
    comment_map = {}

    for comment in comments:
        comment_map[comment.id] = {
            "id": comment.id,
            "author": comment.author.username,
            "content": comment.content,
            "replies": []
        }

    tree = []
    for comment in comments:
        if comment.parent_id:
            comment_map[comment.parent_id]["replies"].append(
                comment_map[comment.id]
            )
        else:
            tree.append(comment_map[comment.id])

    return tree

Why this works well

✅ 1 query per post, regardless of depth

✅ No recursive database calls

✅ Scales well with deep threads

2. The Math — Last 24h Leaderboard Query
Design choice

Karma is stored as immutable transactions, not as counters on the User model.
This avoids stale data and allows time-based aggregation.

Django ORM QuerySet (Used in Project)
from django.utils.timezone import now
from datetime import timedelta
from django.db.models import Sum

last_24_hours = now() - timedelta(hours=24)

leaderboard = (
    KarmaTransaction.objects
    .filter(created_at__gte=last_24_hours)
    .values("user__id", "user__username")
    .annotate(total_karma=Sum("points"))
    .order_by("-total_karma")[:5]
)

Equivalent SQL (Conceptual)
SELECT user_id, SUM(points) AS total_karma
FROM karma_transaction
WHERE created_at >= NOW() - INTERVAL '24 HOURS'
GROUP BY user_id
ORDER BY total_karma DESC
LIMIT 5;

Why this approach

✅ No cached “daily karma” field

✅ Always accurate

✅ Time-windowed analytics become trivial

✅ Easy to extend (7-day, monthly leaderboards)

3. The AI Audit — Example of Catching & Fixing AI Mistakes
What the AI initially suggested (problematic)

AI-generated code attempted to calculate the leaderboard by:

Storing a daily_karma integer field on the User model

Incrementing it on every like

user.daily_karma += 5
user.save()

Why this was wrong

❌ Violates the problem constraint

❌ Prone to race conditions

❌ Hard to reset accurately at 24h boundaries

❌ No audit trail of how karma was earned

How I fixed it

I replaced the counter-based approach with transaction-based accounting:

KarmaTransaction.objects.create(
    user=post.author,
    source_type=KarmaTransaction.POST_LIKE,
    source_id=post.id,
    points=5
)


Then computed leaderboard dynamically using aggregation queries (shown above).

Result

✅ Concurrency-safe

✅ Auditable

✅ Time-based analytics supported


✅ Matches real production systems
