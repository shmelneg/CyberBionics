from django.urls import path, include
from . import views

urlpatterns = [
    path('index/', views.index, name='index-view'),
    path('bio/<name>/', views.bio, name='bio'),
    path('lesson_1/<parameters>/', include('lesson_1.urls')),
]
