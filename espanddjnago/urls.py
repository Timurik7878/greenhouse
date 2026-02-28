from django.urls import path
from . import views

urlpatterns = [
    path('<str:state>/', views.control),
    path('', views.index, name='index'),
]