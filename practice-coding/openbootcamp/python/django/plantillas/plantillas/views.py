from django.shortcuts import render

def simple(request):
    return render(request,'simple.html',{})

def dinamic(request, name):
    categories = ['development','design','marketing']
    context = {
        'name' : name,
        'categories' : categories
        }
    return render(request,'dinamic.html', context) 