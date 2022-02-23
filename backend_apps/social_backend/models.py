from django.db import models
from django.contrib.auth.models import User

class CommentBase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.CharField(max_length=500)
    # timestamp = models.DateTimeField(auto_now_add=True)
    # likes = models.CharField(max_length=1000)

    class Meta:
        abstract = True
    

class Comment(CommentBase):
    video_id = models.CharField(max_length=500)

class Response(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True

class Reply(Response, CommentBase):
    pass

class ReplyID(models.Model):
    reply = models.ForeignKey(Reply, on_delete=models.CASCADE, blank=True, null=True)
    class Meta:
        abstract = True

class Like(Response, ReplyID):
    pass

class Dislike(Response, ReplyID):
    pass
