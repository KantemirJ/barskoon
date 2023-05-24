from django.shortcuts import render
from main.models import Employee


def employee_page(request):
    employees = Employee.objects.all()
    context = {'employees': employees}
    return render(request, 'employee_page.html', context)