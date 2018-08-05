"""Definiuje wzorce adresów URL dla aplikacji users."""

from django.conf.urls import url, re_path
from django.contrib.auth.views import login

from . import views

urlpatterns = [
    # Strona logowania.
    re_path(r'^login/$', login, {'template_name': 'users/login.html'}, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    # Strona rejestracji.
    url(r'^register/$', views.register, name='register'),
]