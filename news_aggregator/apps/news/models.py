from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.CharField(max_length=100)
    published_at = models.DateTimeField(auto_now_add=True)
    source = models.CharField(max_length=100)
    url = models.URLField(max_length=500)

    def __str__(self):
        return self.title