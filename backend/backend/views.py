from django.shortcuts import render
from django.conf import settings

def home(request):
    image_url = settings.MEDIA_URL + 'images/randompic1.png'
    return render(request, 'index.html', {'image_url': image_url})
