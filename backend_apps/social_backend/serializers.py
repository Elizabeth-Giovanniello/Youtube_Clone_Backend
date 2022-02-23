from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Comment, Reply, Like, Dislike


class UserSerializer(serializers.ModelSerializer):
  class Meta:
     model = User
     fields = ['id', 'username']


class ResponseSerializer(serializers.ModelSerializer):

  user = UserSerializer(many=False, read_only=True)
  likes = serializers.SerializerMethodField()
  dislikes = serializers.SerializerMethodField()

  def get_likes(self, response):
    likes = Like.objects.filter(comment=response)
    return LikeSerializer(likes, many=True).data

  def get_dislikes(self, response):
    dislikes = Dislike.objects.filter(comment=response)
    return DislikeSerializer(dislikes, many=True).data



class LikeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Like
    fields = ['user']
    
class DislikeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Dislike
    fields = ['user']

class CommentSerializer(ResponseSerializer):

  class Meta:
    model = Comment
    fields= ['user', 'likes', 'dislikes', 'body', 'id']



class ReplySerializer(ResponseSerializer):

  class Meta:
    model = Reply
    fields = ['user', 'likes', 'dislikes', 'body', 'id', 'comment']

  def get_likes(self, response):
    likes = Like.objects.filter(reply=response)
    return LikeSerializer(likes, many=True).data

  def get_dislikes(self, response):
    dislikes = Dislike.objects.filter(reply=response)
    return DislikeSerializer(dislikes, many=True).data
