from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('upload_tape/',views.upload_tape,name='upload_tape'),
]


