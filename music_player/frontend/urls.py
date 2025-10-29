from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('join/', views.join_room, name="join-room"),
    path('create/', views.create_room, name="create-room"),
]