from django.urls import path, include
from . import views

urlpatterns = [
    path('home/', views.home, name='home-view'),
    path('book/<title>/', views.book, name='book'),
    path('lesson_2/<parameters>/', include('lesson_2.urls')),
]
