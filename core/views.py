# Create your views here.
# from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    context = {
        'visitor': request.GET.get('name', 'guest')
    }
    return render(request, 'core/home.html', context) # Day 6, templates

# def home(request):
#     return HttpResponse(f"Home page — You used {request.method}") # Day 5

# def home(request):
#     return HttpResponse("Home page") # Day 4


def about(request):
    context = {
        'visitor': request.GET.get('name', 'stranger')
    }
    return render(request, 'core/about.html', context) # Day 6, templates

# def about(request):
#     visitor = request.GET.get('name', 'stranger')
#     return HttpResponse(f"About page — Hello, {visitor}!") # Day 5

# def about(request):
#     return HttpResponse("About page") # Day 4


def post_detail(request, post_id):
    context = {
        'post_id': post_id
    }
    return render(request, 'core/post_detail.html', context) # Day 6, templates

# def post_detail(request, post_id):
#     return HttpResponse(f"Viewing post #{post_id} via {request.method}") # Day 5

# def post_detail(request, post_id):
#     return HttpResponse(f"Post ID: {post_id}") # Day 4


def projects(request):
    project_list = [
        {'name': 'Contact Book', 'status': 'Done'},
        {'name': 'Hello Django', 'status': 'Done'},
        {'name': 'Multipage Site', 'status': 'In progress'},
    ]
    return render(request, 'core/projects.html', {'projects': project_list})