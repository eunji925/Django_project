from django.urls import path
from . import views

# urlpatterns = [
#     path("", views.see_all_tweets), # root 경로\
# ]

urlpatterns = [
    path('', views.see_all_tweets,),
    path('api/v1/tweets/', views.TweetListView.as_view()),
    path('api/v1/users/<int:user_id>/tweets/', views.UserTweetListView.as_view()),
]