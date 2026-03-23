from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_kfman, name='all_kfman'),
]
