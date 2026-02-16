from rest_framework import generics
from .models import Post
from .serializers import PostSerializer, PostDetailSerializer


class PostListView(generics.ListAPIView):
    queryset = Post.objects.filter(status="published").order_by("-created_at")
    serializer_class = PostSerializer
    


class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = "slug"
