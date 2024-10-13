from rest_framework.serializers import ModelSerializer, SerializerMethodField
from users.serializers import TinyUserSerializer
from .models import Tweet, Like


class TweetSerializer(ModelSerializer):
    user = TinyUserSerializer(read_only=True)

    class Meta:
        model = Tweet
        fields = "__all__"


class TweetDetailSerializer(ModelSerializer):
    user = TinyUserSerializer(read_only=True)
    is_owner = SerializerMethodField()
    is_liked = SerializerMethodField()

    class Meta:
        model = Tweet
        fields = (
            "payload",
            "user",
            "is_owner",
            "is_liked",
        )

    def get_is_owner(self, tweet):
        request = self.context["request"]
        if not request.user.username:
            return False
        return tweet.user == request.user

    def get_is_liked(self, tweet):
        request = self.context["request"]
        if not request.user.username:
            return False
        return Like.objects.filter(user=request.user, tweet=tweet).exists()