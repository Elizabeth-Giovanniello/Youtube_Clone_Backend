from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Comment, Reply, Like, Dislike
from .serializers import CommentSerializer, LikeSerializer, ReplySerializer
from django.contrib.auth.models import User
from .views_helpers import like_helper, get_response_helper, choose_serializer, add_like_helper

GET = 'GET'
POST = 'POST'
PUT = 'PUT'
DELETE = 'DELETE'

# COMMENTS

@api_view([GET])
@permission_classes([AllowAny])
def get_all_comments(request, video_id):
  comments = Comment.objects.filter(video_id = video_id)
  viscomments = {comment for comment in comments}
  serializer = CommentSerializer(comments, many=True)
  return Response(serializer.data)


@api_view([POST])
@permission_classes([IsAuthenticated])
def add_comment(request):
  serializer = CommentSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save(user=request.user)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view([PUT, DELETE])
@permission_classes([IsAuthenticated])
def edit_comment(request, comment_id):
  comment = Comment.objects.get(pk=comment_id)
  if request.user == comment.user:
    if request.method == PUT:
      serializer = CommentSerializer(comment, request.data)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == DELETE:
      comment.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)
  else:
    return Response(status=status.HTTP_401_UNAUTHORIZED)



# REPLIES

@api_view([GET])
@permission_classes([AllowAny])
def get_all_replies(request, comment_id):
  replies = Reply.objects.filter(comment_id = comment_id)
  serializer = ReplySerializer(replies, many=True)
  return Response(serializer.data)


@api_view([POST])
@permission_classes([IsAuthenticated])
def add_reply(request):
  serializer = ReplySerializer(data=request.data)
  if serializer.is_valid():
    serializer.save(user=request.user)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view([PUT, DELETE])
@permission_classes([IsAuthenticated])
def edit_reply(request, reply_id):
  reply = Reply.objects.get(pk=reply_id)
  if request.user == reply.user:
    if request.method == PUT:
      serializer = ReplySerializer(reply, request.data)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == DELETE:
      reply.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)
  else:
    return Response(status=status.HTTP_401_UNAUTHORIZED)


#LIKES

@api_view([PUT])
@permission_classes([IsAuthenticated])
def toggle_like(request, type, response_id):
  like = like_helper(type, response_id, request.user)
  dislike = like_helper(type, response_id, request.user, False)
  response = get_response_helper(type, response_id)
  response_status = None

  if like:
    like.delete()
    response_status=status.HTTP_204_NO_CONTENT

  else:
    new_like = add_like_helper(type, response, request.user)
    new_like.save()
    response_status=status.HTTP_201_CREATED 

    if dislike:
      dislike.delete()
  
  serializer = choose_serializer(type, response)
  return Response(serializer.data, response_status)


@api_view([PUT])
@permission_classes([IsAuthenticated])
def toggle_dislike(request, type, response_id):
  like = like_helper(type, response_id, request.user)
  dislike = like_helper(type, response_id, request.user, False)
  response = get_response_helper(type, response_id)
  response_status = None

  if dislike:
    dislike.delete()
    response_status=status.HTTP_204_NO_CONTENT

  else:
    new_dislike = add_like_helper(type, response, request.user, False)
    new_dislike.save()
    response_status=status.HTTP_201_CREATED 

    if like:
      like.delete()
  
  serializer = choose_serializer(type, response)
  return Response(serializer.data, response_status)