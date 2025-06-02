# Django imports
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.auth import get_user_model

# Image processing imports
from PIL import Image, ImageOps
from io import BytesIO

# File processing imports
from django.core.files.base import ContentFile

# Other imports
from django.utils.translation import gettext as _
import os


User = get_user_model()


def generate_username_from_email(email):
    """
    Generate a username from the email address.
    If the username already exists, append a number to make it unique.

    Args:
        email (str): The email address from which to generate the username.
    """
    base_username = email.split('@')[0]
    username = base_username
    
    username = ''.join(c for c in base_username if c.isalnum() or c in '._-')

    existing_usernames = User.objects.filter(username__iexact=username).exists()
    if existing_usernames:
        # If the username already exists, append a number to make it unique
        counter = 1
        while User.objects.filter(username__iexact=username).exists():
            username = f"{base_username}{counter}"
            counter += 1

    return username




def optimize_image_quality(image, save_path=None, max_size=(1024, 1024), quality=85):
    """
    Optimize the image quality, resize it, and return a ContentFile.

    Args:
        image (File): The image file to be optimized.
        save_path (str): Optional save path for testing purposes.
        max_size (tuple): The maximum width and height of the image. Default is (1024, 1024).
        quality (int): The quality of the image (1-100). Default is 85.

    Returns:
        ContentFile: The optimized image in file-like format.
    """
    if not image:
        raise ValueError(_("No image provided for optimization."))
    if not hasattr(image, 'read'):
        raise ValueError(_("Provided file is not a valid image."))

    try:
        # Open the image using Pillow
        with Image.open(image) as img:
            # Correct the orientation based on EXIF data
            img = ImageOps.exif_transpose(img)

            # Convert to RGB mode if necessary
            if img.mode in ('RGBA', 'LA', 'P'):
                img = img.convert('RGB')

            # Resize the image while maintaining the aspect ratio
            if img.size[0] > max_size[0] or img.size[1] > max_size[1]:
                img.thumbnail(max_size, Image.Resampling.LANCZOS)

            # Save the optimized image to an in-memory buffer
            buffer = BytesIO()
            img_format = img.format if img.format else 'JPEG'
            img.save(buffer, format=img_format, quality=quality, optimize=True)
            buffer.seek(0)

            # Optional: Save to a path for debug or testing purposes
            if save_path:
                with open(save_path, 'wb') as f:
                    f.write(buffer.getvalue())

            data = {
                'ContentFile': ContentFile(buffer.read(), name=image.name),
                # Size of the image in bytes
                'size': buffer.tell(),
                'format': img_format,
            }

            # Return the optimized image as a ContentFile
            return data

    except Exception as e:
        raise ValueError(_("Error occurred while optimizing image: %s") % str(e))