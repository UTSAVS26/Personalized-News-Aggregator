from django.test import TestCase
from news.models import Article

class ArticleModelTests(TestCase):

    def test_string_representation(self):
        article = Article(title="Sample Title")
        self.assertEqual(str(article), article.title)