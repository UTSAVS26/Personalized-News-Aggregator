from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from news.models import Article

class ArticleAPITests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.article = Article.objects.create(
            title="Test Article",
            content="Test Content",
        )

    def test_get_articles(self):
        response = self.client.get(reverse('article-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_article_detail(self):
        response = self.client.get(reverse('article-detail', args=[self.article.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)