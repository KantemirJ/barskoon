from django.shortcuts import render
from .models import Ad


def index(request):
    ads = Ad.objects.all().order_by('-date')[:5]
    context = {"ads": ads}

    return render(request, 'main.html', context)
