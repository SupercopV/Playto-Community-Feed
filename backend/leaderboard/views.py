from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils.timezone import now
from datetime import timedelta
from django.db.models import Sum

from karma.models import KarmaTransaction
from .serializers import LeaderboardSerializer

class LeaderboardView(APIView):
    def get(self, request):
        last_24_hours = now() - timedelta(hours=24)

        leaderboard = (
            KarmaTransaction.objects
            .filter(created_at__gte=last_24_hours)
            .values("user__id", "user__username")
            .annotate(total_karma=Sum("points"))
            .order_by("-total_karma")[:5]
        )

        data = [
            {
                "user_id": row["user__id"],
                "username": row["user__username"],
                "total_karma": row["total_karma"]
            }
            for row in leaderboard
        ]

        return Response(data)

# Create your views here.
