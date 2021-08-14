from django.shortcuts import render
from django.http import HttpResponse
from .models import Project,Details,Education,Experience
from django.http import (Http404, HttpResponse)

def index(request):
    details=Details.objects.all()
    return render(request,'main/index.html',{'details':details})

def projects(request):
    project_results=Project.objects.all()
    return render(request,'main/projects.html',{"project_results":project_results})

def resume(request):
    details=Details.objects.all()
    project_results=Project.objects.all()
    education=Education.objects.all()
    experience=Experience.objects.all()
    context={
        "details":details,
        "education":education,
        "experience":experience,
        "project_results":project_results
    }
    return render(request,'main/resume.html',context)

def contact(request):
    project_results=Project.objects.all()
    return render(request,'main/contact.html',{"project_results":project_results})

def project(request,id):
    try:
        project = Project.objects.get(id=id)
    except DoesNotExist:
        raise Http404()
    return render(request, 'main/project.html',{"project":project})