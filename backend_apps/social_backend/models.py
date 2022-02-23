from django.db import models
from django.contrib.auth.models import User

#FIXME user_id_id etc

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video_id = models.CharField(max_length=500)
    body = models.CharField(max_length=500)

class Response(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True

class Reply(Response):
    body = models.CharField(max_length=500)

class ReplyID(models.Model):
    reply = models.ForeignKey(Reply, on_delete=models.CASCADE, blank=True, null=True)
    class Meta:
        abstract = True

class Like(Response, ReplyID):
    pass

class Dislike(Response, ReplyID):
    pass
