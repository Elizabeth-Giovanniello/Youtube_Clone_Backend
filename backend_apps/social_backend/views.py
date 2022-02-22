from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view, permission_classes
from .models import Comment, Reply, Like, Dislike
from .serializers import CommentSerializer, ReplySerializer, LikeSerializer, DislikeSerializer
from django.contrib.auth.models import User


@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_comments(request):
  comments = Comment.objects.all()
  serializer = CommentSerializer(comments, many=True)
  return Response(serializer.data)




@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_comment(request):
  serializer = CommentSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save(user=request.user)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

