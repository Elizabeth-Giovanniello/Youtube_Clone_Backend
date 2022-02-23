from .models import Comment, Reply, Like, Dislike
from .serializers import CommentSerializer, ReplySerializer


def like_helper(type, response_id, user, like=True):
  if type == "comments":
    if like:
      return Like.objects.filter(comment=response_id, user=user)
    else:
      return Dislike.objects.filter(comment=response_id, user=user)
  elif type == "replies":
    if like:
      return Like.objects.filter(reply=response_id, user=user)
    else:
      return Dislike.objects.filter(reply=response_id, user=user)


def get_response_helper(type, response_id):

  if type == "comments":
    return Comment.objects.get(pk=response_id)

  elif type == "replies":
    return Reply.objects.get(pk=response_id)


def choose_serializer(type, response):

  if type == "comments":
    return CommentSerializer(response)

  elif type == "replies":
    return ReplySerializer(response)
    

def add_like_helper(type, response, user, like=True):

  if type == "comments":
    if like:
      return Like(comment = response, user=user)
    else:
      return Dislike(comment = response, user=user)

  elif type == "replies":
    if like:
      return Like(reply = response, user=user)
    else:
      return Dislike(reply = response, user=user)