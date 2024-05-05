from django.shortcuts import render
from .models import Project
from .models import Profile
from .models import SkillAndKnowledge
from .models import Certificates

def home(request):
    context = {'profile': Profile.objects.first(),'skills': SkillAndKnowledge.objects.all(), 'certificates': Certificates.objects.all(), 'projects': Project.objects.all()}
    #rederencia com os dados no contexto
    return render(request, 'home.html', context)
