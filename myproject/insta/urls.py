from django.urls import path
from .views import addpost, success, view_posts,feed

urlpatterns = [
    path('addpost/', addpost, name="addpost"),
    path('success/', success, name="success"),
    path('feed/', view_posts, name="feed"),

]
