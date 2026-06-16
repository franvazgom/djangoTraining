from django.urls import path
from core import views

# Es una buena práctica colocar el nombre de la aplicación en el urlpatterns
# Esto con el objetivo de evitar ambiguedad en el caso de existir 2 referencias con el mismo nombre
# por ejemplo: ¿Qué pasaría si en otra aplicación se tiene el nombre “visit_us”?
core_urlpatterns = ([
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('visit_us/', views.visit_us, name='visit_us'),
], 'core')
