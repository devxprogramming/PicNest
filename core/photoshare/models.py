from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify

from django.utils import timezone
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.core.files.storage import default_storage as storage

from core.utils import  optimize_image_quality
import os

from rich.pretty import pprint

User = get_user_model()


# Helper functions goes here


class Album(models.Model):
    owner = models.ForeignKey(User, related_name='albums', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    decscription = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_public = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    is_archived = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)
    cover_image = models.ImageField(upload_to='albums/covers/', blank=True, null=True)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title[:10])
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} by {self.owner}"
    
class Photo(models.Model):
    album = models.ForeignKey(Album, related_name='photos', on_delete=models.CASCADE)
    uploader = models.ForeignKey(User, related_name='photos', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photos/')
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    tags = models.ForeignKey('Tag', related_name='photos', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title or f"Photo {self.id} in {self.album.title}"
    


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Tags"
        ordering = ['name']


class ShareLink(models.Model):

    """Model to represent a shareable link for a photo."""

    PERMISSIONS_CHOICES = (
        ('view', 'View Only'),
        ('edit', 'Edit'),
        ('delete', 'Delete')
    )


    photo = models.ForeignKey(Photo, related_name='share_links', on_delete=models.CASCADE)
    link = models.CharField(max_length=200, unique=True)
    shared_by = models.ForeignKey(User, related_name='shared_links', on_delete=models.CASCADE)
    permissions = models.CharField(max_length=50, choices=PERMISSIONS_CHOICES, default='view')
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"Share link for {self.photo.title} - {self.link}"
    


@receiver(pre_save, sender=Photo)
def optimize_photoModel_images(sender, instance, **kwargs):
    """
    Signal to optimize photo images before saving.
    """
    if instance.image:
        original_image = instance.image
        optimized_image = optimize_image_quality(image=original_image, quality=100)

        pprint(f"Optimized image for {instance.title} with size {optimized_image.data['size']} and format {optimized_image.data['format']}")
        
        file_name = os.path.basename(original_image.name)
        instance.image.save(file_name, optimized_image, save=False)