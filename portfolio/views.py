from django.shortcuts import render
from .models import Project
from .models import Profile
from .models import SkillAndKnowledge
from .models import Certificates
from django.http import HttpResponse

def home(request):
    context = {'profile': Profile.objects.first(),'skills': SkillAndKnowledge.objects.all(), 'certificates': Certificates.objects.all(), 'projects': Project.objects.all()[:3]}
    #rederencia com os dados no contexto
    return render(request, 'home.html', context)

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'project_list.html', {'projects': projects}) 