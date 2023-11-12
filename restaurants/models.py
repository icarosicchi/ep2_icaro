from django.db import models
from django.conf import settings


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()  # Usando TextField para armazenar o conteúdo HTML
    poster_url = models.URLField(max_length=200, null=True)
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} ({self.post_date})'

class Review(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    likes = models.IntegerField(default=0)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f'"{self.text}" - {self.author.username}'