from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from users.models import User
from .models import Tweet


class TweetAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password")
        self.tweet = Tweet.objects.create(user=self.user, payload="Test tweet")
        self.tweet_url = reverse("tweet_detail", args=[self.tweet.pk])
        self.tweets_url = reverse("tweets")

    def test_get_tweets(self):
        response = self.client.get(self.tweets_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_tweet(self):
        self.client.force_authenticate(user=self.user)
        data = {"payload": "New tweet"}
        response = self.client.post(self.tweets_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_tweet_detail(self):
        response = self.client.get(self.tweet_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put_tweet(self):
        self.client.force_authenticate(user=self.user)
        data = {"payload": "Updated tweet"}
        response = self.client.put(self.tweet_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["payload"], "Updated tweet")

    def test_delete_tweet(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(self.tweet_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)