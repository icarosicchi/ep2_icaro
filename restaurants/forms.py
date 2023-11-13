from django.forms import ModelForm
from .models import Post, Comment


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'poster_url',
        ]
        labels = {
            'title': 'Título',
            'content': 'Conteúdo',
            'poster_url': 'URL do Poster',
        }

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = [
            'author',
            'text',
        ]
        labels = {
            'author': 'Usuário',
            'text': 'Resenha',
        }