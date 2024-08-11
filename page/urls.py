from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('work/', views.work, name="work"),
    path('contact/', views.contact, name="contact"),
    path('work/<str:pk>', views.project, name="project"),
    path('contact/success', views.contact_success, name="contact_success"),
]
