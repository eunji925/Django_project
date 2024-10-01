from django.contrib import admin
from .models import Tweet, Like


class ElonMuskFilter(admin.SimpleListFilter):
    title = "Check if Tweet Contains Elon Musk!"

    parameter_name = "word"

    def lookups(self, request, model_admin):
        return [
            ("contain", "Contain"),
            ("not_contain", "Don't Contain"),
        ]

    def queryset(self, request, tweets):
        is_contain = self.value()
        if is_contain == "contain":
            return tweets.filter(payload__contains="Elon Musk")
        if is_contain == "not_contain":
            return tweets.exclude(payload__contains="Elon Musk")
        else:
            tweets

@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = ("payload", "total_likes", "user", "created_at", "updated_at",)
    search_fields = ('user__username',)
    list_filter = (ElonMuskFilter, 'created_at',)


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ("user", "tweet", "created_at", "updated_at",)
    readonly_fields = ("created_at","updated_at",)
    list_filter = ("created_at",)
    search_fields = ("user__username",)
