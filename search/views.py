from django.shortcuts import render
from main.models import Ad


def search_info(request):
    form = request.POST.get('header')
    header = Ad.objects.all().filter(name_startswith==form['header'])
    return render(request, 'search/search.html', {'header': header})