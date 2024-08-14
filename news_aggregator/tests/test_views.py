from django.test import TestCase
from django.urls import reverse

class NewsViewTests(TestCase):

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Personalized News Aggregator")

    def test_article_detail_view(self):
        # Assuming you have an article with id=1
        response = self.client.get(reverse('article_detail', args=[1]))
        self.assertEqual(response.status_code, 200)