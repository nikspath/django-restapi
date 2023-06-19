from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer

@api_view(['GET'])
def home(request):
    return Response({'message':"hi thi is home"})


@api_view(['GET'])
def all_post(request):
    posts=Post.objects.all() 
    serializerpost=PostSerializer(posts,many=True)
    return Response({'posts':serializerpost.data})
