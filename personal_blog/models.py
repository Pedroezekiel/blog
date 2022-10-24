from django.db import models


# Create your models here.
class Author(models.Model):
    username = models.CharField(max_length=200, unique=True)
    email = models.EmailField()
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username

class Article(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='articles_author', null=True, blank=True)
    title = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):
        return self.title
