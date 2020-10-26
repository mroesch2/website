from django.urls import path
from . import views

urlpatterns = [
    path("homepage", views.homepage, name="homepage"),
    path("aboutme", views.aboutme, name="aboutme"),
]