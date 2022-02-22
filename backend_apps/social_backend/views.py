from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Comment, Reply, Like, Dislike
from .serializers import CommentSerializer, ReplySerializer, LikeSerializer, DislikeSerializer
from django.contrib.auth.models import User

@api_view(['GET', 'POST'])
def CommentsList(request):
  match request.method:
    case 'GET':
      comments = Comment.objects.all()
      serializer = CommentSerializer(comments, many=True)
      return Response(serializer.data)
    case 'POST':
      serializer = CommentSerializer(data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

