from django.contrib import admin
from .models import Project, SkillAndKnowledge, Certificates, Profile

admin.site.register(Project)
admin.site.register(SkillAndKnowledge)
admin.site.register(Certificates)
admin.site.register(Profile)