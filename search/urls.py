from django.urls import path
from . import views
urlpatterns = [
    path('', views.search_info, name='search_info'),
]