from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Tweet
from users.models import User
from .serializers import TweetSerializer

def see_all_tweets(request):
    tweets = Tweet.objects.all()
    return render(
        request, 
        "all_tweets.html",
        {"tweets" : tweets, "title": "All Tweets"}  
    )

class TweetListView(APIView):
    def get(self, request):
        tweets = Tweet.objects.all()
        serializer = TweetSerializer(tweets, many=True)
        return Response(serializer.data)

class UserTweetListView(APIView):
    def get(self, request, user_id):
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return Response({'error': 'User does not exist'}, status=404)

        tweets = Tweet.objects.filter(user=user)
        serializer = TweetSerializer(tweets, many=True)
        return Response(serializer.data)