from attr import fields
from django import forms
from numpy import require
from models import  *

class AuthorForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Author
        fields = ('id',
                  'username',
                  'email',
                  'password',
                  )

# class ArticleForm(forms.ModelForm):
#     author = models.ForeignKey(Author, related_name='articles_author', required=False)

#     class Meta:
#         models = Article
#         fields = ('id',
#                   'author',
#                   'title',
#                   'body',)
