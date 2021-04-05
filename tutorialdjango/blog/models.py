from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length = 255) #titulo
    slug = models.SlugField(max_length = 255, unique = True) #identificador do post que vai no url
    author = models.ForeignKey(User, on_delete = models.CASCADE) #cria um id para os usuários
    body = models.TextField() #texto do post
    created = models.DateTimeField(auto_now_add = True) #add automaticamente a data e a hora que o post foi criado
    updated = models.DateTimeField(auto_now = True)

    class Meta:
        ordering = ('-created',)
        
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:detail", kwargs = {"slug": self.slug})