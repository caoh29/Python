from django.urls import path
from . import views


urlpatterns = [
    path("", views.tasksofyourlife, name="tasksofyourlife"),
    path("add", views.add, name="add"),
]