from django.shortcuts import render
from main.models import History


def history_page(request):
    histories = History.objects.all()
    context = {'histories': histories}
    return render(request, 'history_page.html', context)