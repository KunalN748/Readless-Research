from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('todos/', views.todos, name='todos'),
    path('load_pdfs/', views.load_pdfs, name='load_pdfs'),
]