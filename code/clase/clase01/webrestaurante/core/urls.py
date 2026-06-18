from django.urls import path
from core import views

core_urlpatterns = ([
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('visit_us/', views.visit_us, name='visit_us'),
], 'core')
