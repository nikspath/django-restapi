from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer
from django.conf import settings
from django.core.mail import send_mail

@api_view(['GET'])
def home(request):
    return Response({'message':"hi thi is home"})


@api_view(['GET'])
def all_post(request):
    posts=Post.objects.all() 
    serializerpost=PostSerializer(posts,many=True)
    return Response({'posts':serializerpost.data})



def send_email_user(request):
    subject = 'welcome to GFG world'
    message = 'thank you for registering in geeksforgeeks.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ["patilnikhil991@gmail.com", ]
    respo=send_mail( subject, message, email_from, recipient_list )
    return Response({"email":respo})
    
