from rest_framework.serializers import ModelSerializer
from .models import Post, User, SubPost, Tag


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class SubPostSerializer(ModelSerializer):
    class Meta:
        model = SubPost
        fields = '__all__'


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
