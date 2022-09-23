from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Post, User, SubPost, Tag


class PostSerializer(ModelSerializer):
    user_info = serializers.ReadOnlyField()
    tags = serializers.StringRelatedField(many=True)
    class Meta:
        model = Post
        fields = '__all__'


class UserSerializer(ModelSerializer):
    post = serializers.StringRelatedField(many=True)
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
