from django.urls import path
from . import views


urlpatterns = [
    path("", views.tasksofyourlife, name="tasksofyourlife"),
]