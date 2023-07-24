from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post,Like


from django.contrib.auth.models import User
from .models import Post, Like

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class PostSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    likes_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'title', 'description', 'content', 'creation_date', 'owner', 'likes_count']

    def get_likes_count(self, post):
        return Like.objects.filter(post=post).count()

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'post', 'user', 'created_date']