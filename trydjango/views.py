import random

from django.http import HttpResponse
from django.template.loader import render_to_string
from articles.models import Article


def home_view(request):
    """
    Take in a request
    Return HTML as a response
    """

    queryset_articles = Article.objects.all()
    print(queryset_articles)
    rundom_id = random.randint(1, 3)
    article_obj = Article.objects.get(id=rundom_id)
    context = {
        "objects_list": queryset_articles,
        "object": article_obj,
        "title": article_obj.title,
        "id": article_obj.id,
        "content": article_obj.content,
    }
    HTML_STRING = render_to_string("home-view.html", context=context)
    return HttpResponse(HTML_STRING)
