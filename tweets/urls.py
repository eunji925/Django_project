from django.urls import path
from . import views

urlpatterns = [
    path("", views.TweetListCreateAPIView.as_view(), name="tweets"),
    path("<int:pk>/", views.TweetDetailAPIView.as_view(), name="tweet_detail"),
]