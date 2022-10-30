from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("task_2/", views.task_2),
    path("task_4/", views.task_4),
    path("task_4/add_review/", views.add_review),
]
