from django.db import models
from django.contrib.auth.models import User



class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video_id = models.CharField(max_length=500)
    body = models.CharField(max_length=500)

class Response(models.Model):
    comment_id = models.ForeignKey(Comment, on_delete=models.CASCADE, blank=True, null=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

class Reply(Response):
    body = models.CharField(max_length=500)

class ReplyID(models.Model):
    reply_id = models.ForeignKey(Reply, on_delete=models.CASCADE, blank=True, null=True)

class Like(Response, ReplyID):
    pass

class Dislike(Response, ReplyID):
    pass
