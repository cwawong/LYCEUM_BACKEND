from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Post
from .serializers import PostSerializer
# Create your views here.

@api_view(['GET'])
def getRoutes(request):
    return Response('Our API')

@api_view(['GET'])
def getPosts(request):
    posts = Post.objects.all()

    serilaizer = PostSerializer(posts, many=True)
    return Response(serilaizer.data)

@api_view(['GET'])
def getPost(request, pk):
    post = Post.objects.get(id=pk)
    print(post)
    serilaizer = PostSerializer(post, many=False)
    return Response(serilaizer.data)

# handsome guy