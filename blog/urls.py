from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="blog-home"),
    path("user/<int:pk>/", views.home, name="user-home"),
    path("about/", views.about, name="blog-about"),
]
