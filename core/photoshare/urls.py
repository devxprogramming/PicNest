from django.urls import path
from . import views


urlpatterns = [
    path('photos/', views.PhotoListView.as_view(), name='photo_list'),
    path('photos/<int:pk>/', views.PhotoDetailView.as_view(), name='photo_detail'),
    path('photos/upload/', views.PhotoUploadView.as_view(), name='photo_upload'),
]
