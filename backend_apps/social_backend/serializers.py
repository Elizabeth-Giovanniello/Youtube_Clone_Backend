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
    fields = ['user_id']
    
class DislikeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Dislike
    fields = ['user_id']

class CommentSerializer(serializers.ModelSerializer):
  user_id = UserSerializer(many=False, read_only=True)
  likes = LikeSerializer(many=True, read_only=True)
  dislikes = DislikeSerializer(many=True, read_only=True)
  class Meta:
    model = Comment
    fields= ['user_id', 'likes', 'dislikes', 'body', 'id']

class ReplySerializer(serializers.ModelSerializer):
  user = UserSerializer(many=False, read_only=True)
  likes = LikeSerializer(many=True, read_only=True)
  dislikes = DislikeSerializer(many=True, read_only=True)
  class Meta:
    model = Reply
    fields = '__all__'