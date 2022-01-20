# Here is where the logic of the code happens


from django.http import HttpResponse
from django.shortcuts import render
from projects.models import Project


def all_projects(request):
    # Query the database to return all the projects objects
    projects = Project.objects.all()
    return render(request, 'projects/all_projects.html', {'projects': projects})
