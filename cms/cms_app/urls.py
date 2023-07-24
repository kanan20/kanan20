from django.urls import path
from .views import UserCreateView, UserDetailView, PostCreateView, PostDetailView, LikeCreateView, LikeDetailView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
urlpatterns = [
    path('users/', UserCreateView.as_view(), name='user-create'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('posts/', PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('likes/', LikeCreateView.as_view(), name='like-create'),
    path('likes/<int:pk>/', LikeDetailView.as_view(), name='like-detail'),
]