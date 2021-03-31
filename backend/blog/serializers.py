from .models import BlogPost
from rest_framework import routers, serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = '__all__'
        lookup_field = 'slug'
