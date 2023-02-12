from django.shortcuts import render
from .models import Article

def article_home_view(request, id=None):
    article_obj = None
    if id is not None:
        article_obj = Article.objects.get(id=id)
    contest ={
        "object": article_obj
    }
    return render(request, "articles/detail.html", contest)
