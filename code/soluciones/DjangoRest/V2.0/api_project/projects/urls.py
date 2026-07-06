from rest_framework import routers
from django.urls import path, include
from .api import ProjectViewSet
from .api_g import DataTest, ProjectServices

router = routers.DefaultRouter()

router.register('api/projects', ProjectViewSet, 'projects')

# urlpatterns = router.urls

urlpatterns = [
    path('api/', include(router.urls)),
    path('dataTest/', DataTest.as_view()),
    path('projectServices/', ProjectServices.as_view()),
]