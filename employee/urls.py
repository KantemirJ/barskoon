from django.urls import path
from . import views
urlpatterns = [
    path('', views.employee_page, name='employee_page'),
]