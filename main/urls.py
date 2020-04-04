from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.bio, name="bio"),
    path("photos/", views.photos, name="photos"),
]
