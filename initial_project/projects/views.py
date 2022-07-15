from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return HttpResponse('Home')


def projects(request):
    return render(request, 'projects/projects.html')


def project(request, project_id):
    return HttpResponse('Project page: ' + str(project_id))
