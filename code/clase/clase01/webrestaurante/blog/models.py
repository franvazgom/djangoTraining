from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    created = models.DateTimeField(
        auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(
        auto_now=True, verbose_name='Fecha de actualización')

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['-name']

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='Título')
    content = models.TextField(verbose_name='Contenido')
    published = models.DateTimeField(
        default=timezone.now, verbose_name='Fecha de publicación')
    image = models.ImageField(
        upload_to='blog', null=True, blank=True, verbose_name='Imágen')
    author = models.ForeignKey(
        User, verbose_name='Autor', on_delete=models.CASCADE)
    categories = models.ManyToManyField(
        Category, verbose_name='Categorías', related_name='get_posts')
    created = models.DateTimeField(
        auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(
        auto_now=True, verbose_name='Fecha de actualización')

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-published']

    def __str__(self):
        return self.title

    # def author_name(self):
    #     return self.author.first_name + " " + self.author.last_name
