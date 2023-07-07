from django.urls import path
from .views import Registration_view, LoginForms_Views, Logout_View, profile_view

urlpatterns = [
    path('profile/', profile_view, name='profile'),
    path('logout/', Logout_View, name='logout'),
    path('registration/', Registration_view, name='registration'),
    path('login/', LoginForms_Views, name='login')
]
