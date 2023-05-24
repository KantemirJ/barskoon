from django.shortcuts import render
from main.models import Ad


def news_page(request):
    ads = Ad.objects.all()
    context = {"ads": ads}
    return render(request, 'news_page.html', context)
