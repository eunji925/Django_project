from django.urls import path
from . import views

urlpatterns = [
    path("", views.see_all_tweets), # root 경로\
    path("api/v1/tweets",views.get_all_tweets_list),
    path("api/v1/users/<int:user_id>/tweets",views.get_tweets_list),
]