"""drf_jwt_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('authentication.urls')),
    path('api/<str:video_id>/', views.get_all_comments), 
    path('api/comments/', views.add_comment),
    path('api/comments/<int:comment_id>/', views.get_all_replies), 
    path('replies/', views.add_reply),
    path('comments/<int:comment_id>/', views.edit_comment),
    path('replies/<int:reply_id>/', views.edit_reply),
    path('api/<str:type>/<int:response_id>/like/', views.toggle_like),
    path('api/<str:type>/<int:response_id>/dislike/', views.toggle_dislike),
]
