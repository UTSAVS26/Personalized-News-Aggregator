from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'published_at']

class ArticleSummarySerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    summary = serializers.CharField(max_length=1000)