from django.shortcuts import render, redirect, get_object_or_404

# Core Django imports
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model, login, logout, authenticate
from django.http import HttpResponse, JsonResponse
from django.urls import reverse, reverse_lazy

# Rest Framework imports
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes

# Local imports
from .models import Album, Photo, ShareLink, Tag
from .serializer import AlbumSerializer, PhotoSerializer, ShareLinkSerializer, TagSerializer


User = get_user_model()



class AlbumViewSet(ModelViewSet):
    """
    ViewSet for managing albums.
    """
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    

class PhotoViewSet(ModelViewSet):
    """
    ViewSet for managing photos.
    """
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(uploader=self.request.user)
    


class TagViewSet(ModelViewSet):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()


    def perform_create(self, serializer):
        serializer = self.serializer_class
        serializer.is_valid(raise_exception=True)
        serializer.save(created_by=self.request.user)
        return Response(serializer.data, status.HTTP_201_CREATED)