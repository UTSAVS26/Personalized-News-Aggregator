from django.shortcuts import render, get_object_or_404
from .models import Article
import openai
from django.conf import settings

def article_list(request):
    articles = Article.objects.all()
    return render(request, 'news/index.html', {'articles': articles})

def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    
    # Summarize the article using ChatGPT
    openai.api_key = settings.OPENAI_API_KEY
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Summarize the following article: {article.content}",
        max_tokens=150
    )
    summary = response.choices[0].text.strip()
    
    return render(request, 'news/article_detail.html', {'article': article, 'summary': summary})