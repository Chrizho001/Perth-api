from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    tags = serializers.SlugRelatedField(many=True, read_only=True, slug_field="name")

    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "content",
            "created_at",
            "slug",
            "image_url",  #  use this instead of raw image
            "status",
            "tags",
        ]

    def get_image_url(self, obj):
        if obj.image:
            return obj.image.url  #  Cloudinary gives full URL
        return None


class PostDetailSerializer(serializers.ModelSerializer):
    tags = serializers.SlugRelatedField(many=True, read_only=True, slug_field="name")
    similar_posts = serializers.SerializerMethodField()
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "slug",
            "content",
            "created_at",
            "image_url",
            "tags",
            "similar_posts",
        ]

    def get_image_url(self, obj):
        if obj.image:
            return obj.image.url  #  Cloudinary gives full URL
        return None

    
    def get_similar_posts(self, obj):
        similar_qs = (
            Post.objects.filter(tags__in=obj.tags.all()).exclude(id=obj.id).distinct()
        )

        return [
            {
                "slug": post.slug,
                "image_url": post.image.url if post.image else None,
                "title": post.title,
                "created_at": post.created_at,
            }
            for post in similar_qs
        ]
