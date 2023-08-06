from django.urls import path
from data_app1 import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('about/', views.about, name="about"),
    path('upload/', views.upload_document, name='upload_document'),
    path('data_text/',views.data_text, name="data_text"),
    path('signup/',views.SignupPage,name='signup'),
    path('',views.LoginPage,name='login'),
    path('logout/',views.LogoutPage,name='logout'),
]