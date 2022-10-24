from django.shortcuts import get_object_or_404
from rest_framework import generics
from .models import Article,Author
from .serializers import AuthorSerializer, ArticleSerializer

class ListArticles(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class DetailArticles(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

# class UpdateArticles(generics.UpdateAPIView, id):
#     context = {}
#     obj = get_object_or_404(Article)
#     serializer_class = ArticleSerializer
    

class ListAuthor(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorListView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    
    
