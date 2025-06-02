from django.urls import path, include
from . import views

# REST Framework imports
from rest_framework.routers import DefaultRouter
\
router = DefaultRouter()


router.register(r'albums', views.AlbumViewSet, basename='album')


urlpatterns = [
    path('', include(router.urls)),
]

