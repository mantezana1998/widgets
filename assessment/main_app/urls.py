from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('', views.add_widget, name='add_widget'),
    path('', views.delete_widget, name='delete'),
]