from django.urls import path
from .views import todu_list_view, todu_create_view, todu_delete_view, todu_detail_view, todu_edit_view, \
    todu_check_viuw, home_wiuv

urlpatterns = [
    path('', home_wiuv, name='home'),
    path('todu/list/', todu_list_view, name='todu_list'),
    path('todu/create/', todu_create_view, name='todu_create'),
    path('todu/delete/<int:id>/', todu_delete_view, name='todu_delet'),
    path('todu/detail/<int:id>/', todu_detail_view, name='todu_detail'),
    path('todu/edit/<int:id>/', todu_edit_view, name='todu_edit'),
    path('todu/check/<int:id>/', todu_check_viuw, name='todu_check')
]
