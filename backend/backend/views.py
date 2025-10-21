from django.shortcuts import render
from django.conf import settings
import os

def home(request):
<<<<<<< HEAD
    image_url = settings.MEDIA_URL + 'images/randompic1.png'
    return render(request, 'index.html', {'image_url': image_url})
=======
    images_dir = os.path.join(settings.STATICFILES_DIRS[0], 'images')
    image_files = []

    if os.path.exists(images_dir):
        for filename in os.listdir(images_dir):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp')):
                image_files.append(f'images/{filename}')

    return render(request, 'index.html', {'image_files': image_files})
>>>>>>> 0f7385f5ecc00ccc4272f97e0f071e978cce2acc
