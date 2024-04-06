from django.http import HttpResponse
from .models import *


def author_list(request):
    authors = Author.object.all()
    authors_list = ""
    for author in authors:
        authors_list += f"<li>{author.name}</li>"
    return HttpResponse(f"<li>{authors_list}</li>")
