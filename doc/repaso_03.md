## Template tags - Ciclos - If
```python
{% for project in projects %}
...
{% endfor %}

{% if project.link %}
    <p><a href="{{project.link}}" target='_blank'>Más información</a></p>
{% endif %}

# Cuando ya se encuentra configurado el URL patterns.. 
{% url 'core:home' %}
```
## Flujo Django
Se realizó explicación básica del flujo desde el request (solicitud) hasta la respuesta (response)

## Model.py (valores nulos)
```python
link = models.URLField(null=True, blank=True, verbose_name='Liga')
```

## Práctica restaurante
+ Crear proyecto:  webrestaurante
+ Aplicación: core
+ Views: home, about y visit_us
+ Templates: home, about y visit-us
+ Configuración de URLS: core_urlpatterns = ([ .. ], 'core')


## Modelos y relaciones
```python
from django.contrib.auth.models import User
...
    # Un post solo puede tener 1 autor y 1 autor, puede tener "muchos" post
    author = models.ForeignKey(User, verbose_name='Autor', on_delete=models.CASCADE)
    # Un post puede tener "1 o muchas" categorías y una categoría puede tener "0 o muchos" post
    categories = models.ManyToManyField(Category, verbose_name='Categorías', related_name='get_posts')
```
