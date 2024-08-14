from django.shortcuts import render, get_object_or_404
from .models import Article

def index(request):
    articles = Article.objects.all().order_by('-published_at')
    return render(request, 'news/index.html', {'articles': articles})

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'news/article_detail.html', {'article': article})