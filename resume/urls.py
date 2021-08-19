from django.urls import path

from . import views


urlpatterns = [
    path('', views.hompage, name='homepage'),
    path('contact', views.handle_form, name='contact'),
]