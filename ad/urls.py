from django.urls import path, include
from . import views

urlpatterns = [
    path('<int:ad_id>', views.ad_page, name='ad_page')
]