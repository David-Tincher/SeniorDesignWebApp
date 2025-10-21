from django.shortcuts import render
from django.conf import settings
import os

def home(request):
    images_dir = os.path.join(settings.STATICFILES_DIRS[0], 'images')
    image_files = []

    if os.path.exists(images_dir):
        for filename in os.listdir(images_dir):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp')):
                image_files.append(f'images/{filename}')

    return render(request, 'index.html', {'image_files': image_files})
