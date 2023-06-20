from django.urls import path
from .views import todu_list_view

urlpatterns = [
    path('', todu_list_view, name='todu_list')
]
