import logging

from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Post, User, SubPost, Tag





class UserSerializer(ModelSerializer):
    post = serializers.StringRelatedField(many=True)
    class Meta:
        model = User
        fields = '__all__'


class SubPostSerializer(ModelSerializer):
    user_info = serializers.ReadOnlyField()
    class Meta:
        model = SubPost
        fields = '__all__'


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class PostSerializer(ModelSerializer):
    user_info = serializers.ReadOnlyField()
    tags = TagSerializer(read_only=False, many=True)
    class Meta:
        model = Post
        fields = '__all__'

    def create(self, data):
        logging.critical(data)
        post = Post(title=data['title'], message=data['message'], user=data['user'])
        post.save()
        post.tags.set([Tag.objects.get(name=tagName).id for tagName in [tag['name'] for tag in data['tags']]])
        return post
