from django.shortcuts import render

tasks = ["dormir", "estudiar", "trabajar", "reproducir", "morir"]
# Create your views here.
def tasksofyourlife(request, tasks):
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })