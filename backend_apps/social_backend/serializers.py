from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Comment, Reply, Like, Dislike

class UserSerializer(serializers.ModelSerializer):
  class Meta:
     model = User
     fields = ['id', 'username']

class LikeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Like
    fields = ['user']
    
class DislikeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Dislike
    fields = ['user']

class CommentSerializer(serializers.ModelSerializer):
  user = UserSerializer(many=False, read_only=True)
  likes = serializers.SerializerMethodField()
  dislikes = serializers.SerializerMethodField()
  class Meta:
    model = Comment
    fields= ['user', 'likes', 'dislikes', 'body', 'id']

  def get_likes(self, response):
    likes = Like.objects.filter(comment=response)
    return LikeSerializer(likes, many=True).data

  def get_dislikes(self, response):
    dislikes = Dislike.objects.filter(comment=response)
    return DislikeSerializer(dislikes, many=True).data

class ReplySerializer(serializers.ModelSerializer):
  user = UserSerializer(many=False, read_only=True)
  class Meta:
    model = Reply
    fields = ['user', 'like_set', 'dislike_set', 'body', 'id', 'comment']