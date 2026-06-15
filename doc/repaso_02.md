## ORM
Definición, ventajas

###	Creación del MODELO models.py
```python
class Project (models.Model):
    title = models.CharField(max_length=100, verbose_name='Título')
    description = models.TextField(verbose_name='Descripción')
    # upload_to -> ruta donde se guardarán las imágenes
    image = models.ImageField(verbose_name='Imágen', upload_to='project')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')

    class Meta: 
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'

        ordering = ['-created']
    
    def __str__(self):
        return self.title
```
## Comandos desde consola
```bash
python manage.py makemigrations
python manage.py migrate
```

## settings.py
librería:  django-cleanup 

```python
INSTALLED_APPS = [
    ... 
    'django.contrib.staticfiles',
    'django_cleanup',
    'core',
    'project',
]

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
```

## admin.py 
```python
from django.contrib import admin
from .models import Project

class ProjectAdmmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Project, ProjectAdmmin)
```

## views.py
```python
def project(request):
    projects = Project.objects.all() #Queryset 
    return render(request, "project/project.html", {'projects': projects})
```

## urls.py
urls.py (solo se hace en modo DEBUG)
```python
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
```

## Template tags
```python
    {% for project in projects %}    
        ...
        <img class="zzzzzzz" src="{{ project.image.url }}" alt="" />
        ... 
        {{project.title}}
        ...
    {% endfor %}
```