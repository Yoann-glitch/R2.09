from django.shortcuts import render
from .models import Article

def liste_articles(request):
    articles = Article.objects.all()
    return render(request, 'nom_de_l_application/liste_articles.html', {'articles': articles})