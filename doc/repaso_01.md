## Comandos desde consola
```bash
django-admin startproject

python manage.py startapp

python manage.py runserver

python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser
```

## settings.py 
```python
LANGUAGE_CODE = 'es'
TIME_ZONE = 'America/Mexico_City'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

INSTALLED_APPS = [
...
]
```

## views.py
```python
from django.shortcuts import render
def home(request):
    return render(request, 'PATH')
```

## urls.py
```python
urlpatterns = [
    path('PATH', VIEW, name='NAME'),
]
```

## Template tags
```python
# Plantilla padre
{% block content %} {% endblock %}

# Plantilla heredada
{% extends 'core/base.html' %}

# urls
{% url 'nombre' %}

# Archivos estáticos
{% load static %}
< ... href=" {% static 'PATH' %} " />

```