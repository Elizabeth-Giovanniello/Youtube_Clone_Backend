from django.contrib import admin
from .models import Comment, Reply, Like, Dislike

admin.site.register([Comment, Reply, Like, Dislike])