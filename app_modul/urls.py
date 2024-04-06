from django.urls import path
from .views import author_list

urlpatterns = [
    path('authors/', author_list, name='author_list'),
]
