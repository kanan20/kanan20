from rest_framework import generics, permissions
from django.contrib.auth.models import User
from .models import Post, Like
from .serializers import UserSerializer, PostSerializer, LikeSerializer
from .permissions import IsPostOwner, IsLikeOwner
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
class UserCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')

        if not username or not password or not email:
            return Response({'error': 'Please provide all required fields: username, password, email'}, status=400)

        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username already exists. Please choose a different username.'}, status=400)

        try:
            user = User.objects.create_user(username=username, password=password, email=email)
            return Response({'message': 'User created successfully'}, status=201)
        except Exception as e:
            return Response({'error': 'An error occurred while creating the user.'}, status=500)

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PostCreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return []
        return [permissions.IsAuthenticated(), IsPostOwner()]

class LikeCreateView(generics.CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]

class LikeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsLikeOwner()]