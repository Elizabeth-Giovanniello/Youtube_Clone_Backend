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
    path('auth/', include('authentication.urls')),
    path('get_comments/<str:video_id>/', views.get_all_comments), 
    path('add_comment/', views.add_comment),
    path('view_replies/<int:comment_id>/', views.get_all_replies), 
    path('add_reply/', views.add_reply),
    path('edit_comment/<int:comment_id>/', views.edit_comment),
    path('edit_reply/<int:reply_id>/', views.edit_reply),
    path('like/<str:type>/<int:response_id>/', views.toggle_like),
    path('dislike/<str:type>/<int:response_id>/', views.toggle_dislike),
]
