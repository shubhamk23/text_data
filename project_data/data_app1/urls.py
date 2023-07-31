from django.urls import path
from data_app1 import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name="about"),
    path('upload/', views.upload_document, name='upload_document'),
    path('data_text/',views.data_text, name="data_text")
]