from rest_framework.serializers import ModelSerializer
from .models import User

class TinyUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "id",
        )


class DetailUserSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = (
            "id",
            "password",
            "is_superuser",
            "is_staff",
            "is_active",
            "first_name",
            "last_name",
            "groups",
            "user_permissions",
        )