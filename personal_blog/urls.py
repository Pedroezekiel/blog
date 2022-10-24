from django.urls import path
from .views import *
urlpatterns = [
    path('',ListArticles.as_view()),
    path('<int:pk>',DetailArticles.as_view()),
    path('author/',ListAuthor.as_view()),
    path('author/<int:pk>/',AuthorListView.as_view()),
]
