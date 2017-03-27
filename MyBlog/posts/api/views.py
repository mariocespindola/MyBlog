from rest_framework.generics import ListAPIView,RetrieveAPIView

from MyBlog.posts.models import Post
from .serializers import PostDetailSerializer, PostListSerializer


class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'


class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer



