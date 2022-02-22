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
    fields = ['id', 'user_id', 'reply_id', 'comment_id']
    
class DislikeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Dislike
    fields = ['id', 'user_id', 'reply_id', 'comment_id']

class CommentSerializer(serializers.ModelSerializer):
  user = UserSerializer(many=False, read_only=True)
  likes = LikeSerializer(many=True, read_only=True)
  dislikes = DislikeSerializer(many=True, read_only=True)
  class Meta:
    model = Comment
    fields=  '__all__'

class ReplySerializer(serializers.ModelSerializer):
  user = UserSerializer(many=False, read_only=True)
  likes = LikeSerializer(many=True, read_only=True)
  dislikes = DislikeSerializer(many=True, read_only=True)
  class Meta:
    model = Reply
    fields = ['id','body', 'user_id', 'comment_id']