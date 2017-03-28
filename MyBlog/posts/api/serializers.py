from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField

from MyBlog.posts.models import Post


class PostCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'publish',
        ]


post_detail_url = HyperlinkedIdentityField(
    view_name='post-api:detail',
    lookup_field='slug',
)


class PostDetailSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'url',
            'id',
            'title',
            'slug',
            'content',
            'publish',
        ]


class PostListSerializer(ModelSerializer):
    url = post_detail_url

    class Meta:
        model = Post
        fields = [
            'url',
            'user',
            'title',
            'content',
            'publish',
        ]
