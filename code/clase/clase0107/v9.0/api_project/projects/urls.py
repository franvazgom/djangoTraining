from rest_framework import routers
from .api import ProjectViewSet
from django.urls import path, include
from projects.api_g import DataTest, ProjectServices

router = routers.DefaultRouter()

router.register('api/projects', ProjectViewSet, 'projects')

# urlpatterns = router.urls
urlpatterns = [
    path('', include(router.urls)),
    path('dataTest/', DataTest.as_view()),
    path('projectServices/', ProjectServices.as_view()),
]
