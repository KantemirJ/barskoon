from django.shortcuts import render
from main.models import Employee
from .models import CommentPerson
from .forms import CommentPersonForm


def person_page(request, person_id):
    person = Employee.objects.get(id=person_id)
    user = request.user.username
    if request.method == 'POST':
        form = CommentPersonForm(request.POST)
        if form.is_valid():
            com = CommentPerson(username=request.user, name=person, comment=request.POST['comment'])
            com.save()
    form = CommentPersonForm()
    comments = CommentPerson.objects.all().filter(name=person).order_by('-id')[:10]
    context = {'person': person, 'user': person, 'form': form, 'comments': comments}
    return render(request, 'person/person_page.html', context)