from django.urls import path
from . import views
from .views import create_article

urlpatterns = [
    path('', views.index, name='index'),
    path('creat/', create_article),
]
