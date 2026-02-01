from rest_framework import serializers

class LeaderboardSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    username = serializers.CharField()
    total_karma = serializers.IntegerField()
