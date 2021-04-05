from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length = 255) #titulo
    slug = models.SlugField(max_length = 255, unique = True) #identificador do post que vai no url
    author = models.ForeignKey(User, on_delete = models.CASCADE) #cria um id para os usuários
    body = models.TextField() #texto do post
    created = models.DateTimeField(auto_now_add = True) #add automaticamente a data e a hora que o post foi criado
    updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title