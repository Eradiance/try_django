from django.shortcuts import render
from .models import Article


def article_create_view(request):
    context ={}
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        article_obj = Article.objects.create(title=title, content=content)
        context["object"] = article_obj
        context["created"] = True
    return render(request, "articles/create.html", context=context)

def article_search_view(request):
    query_dict = request.GET
    query = query_dict.get("query")
    try:
        query = int(query_dict.get("query"))
    except:
        query = None
    article_obj = None
    if query is not None:
        article_obj = Article.objects.get(id=query)
    context = {
        "object": article_obj
    }
    return render(request, "articles/search.html", context)

def article_home_view(request, id=None):
    article_obj = None
    if id is not None:
        article_obj = Article.objects.get(id=id)
    context ={
        "object": article_obj
    }
    return render(request, "articles/detail.html", context)
