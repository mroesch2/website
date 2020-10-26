from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("aboutme", views.aboutme, name="aboutme"),
    path("resume", views.resume, name="resume"),
]