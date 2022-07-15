from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


projectsList = [
    {
        'id': 1,
        'title': 'Ecommerce Website',
        'description': 'Fully functional e-commerce website.',
        'topRated': True
    },
    {
        'id': 2,
        'title': 'Portfolio Website',
        'description': 'A personal website to write articles and display.',
        'topRated': False
    },
    {
        'id': 3,
        'title': 'Social Network',
        'description': 'An open source project built by the community.',
        'topRated': False
    }
]


def home(request):
    return HttpResponse('Home')


def projects(request):
    context = {
        'name': 'calki',
        'age': 25,
        'projectsList': projectsList
    }
    return render(request, 'projects/projects.html', context=context)


def project(request, project_id):
    projectObject = list(filter(lambda l: l['id'] == project_id, projectsList))
    print(projectObject)
    return render(request, 'projects/project.html', {'project': projectObject and projectObject[0] or False})
