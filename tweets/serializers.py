from rest_framework import serializers
from .models import Tweet

class TweetSerializer(serializers.Serializer):
    
    id = serializers.IntegerField()
    user = serializers.CharField(source='user.username')
    payload = serializers.CharField()
    created_at = serializers.DateTimeField()