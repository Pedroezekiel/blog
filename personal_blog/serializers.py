from rest_framework import serializers, fields
from .models import Author, Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'author',
            'title',
            'body',
        )
        model = Article


class AuthorSerializer(serializers.ModelSerializer):
    articles_author = ArticleSerializer(many=True, required=False)

    class Meta:
        fields = (
            'id',
            'username',
            'email',
            'password',
            'articles_author',
        )
        model = Author

    def create(self, validated_data):
        # articles_data = validated_data.pop('articles_author')
        author = Author.objects.create(**validated_data)
        # for article_data in articles_data:
        #     Article.objects.create(author=author, *article_data)
        return author

    # def delete(self, validated_data):
    #     author = Author.objects.delete(**validated_data)
    #     return author



