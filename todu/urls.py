from django.urls import path
from .views import todu_list_view, todu_create_view

urlpatterns = [
    path('', todu_list_view, name='todu_list'),
    path('todu/create/', todu_create_view, name='todu_create')
]
