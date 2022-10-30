from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("task_1/", views.task_1),
    path("starwars/", views.starwars),
    path("luke/", views.luke),
    path("leia/", views.leia),
    path("han/", views.han),
    path("task_3/", views.task_3),
    path("task_5/", views.task_5),
    path("task_7/", views.task_7),
    path("task_8/", views.task_8),
]
