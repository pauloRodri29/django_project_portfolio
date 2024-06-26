from django.db import models

class Project(models.Model): # Modelo de Projetos
    title = models.CharField(max_length=100)
    description = models.TextField()
    url = models.URLField()

    def __str__(self):
        return self.title

class SkillAndKnowledge(models.Model):# Modelo de Conhecimentos e Habilidades
    title = models.CharField(max_length=100)
    imageURL = models.URLField()
    
    def __str__(self):
        return self.title

class Certificates(models.Model):# Modelo de Certificados
    title = models.CharField(max_length=100)
    organizer = models.CharField(max_length=50)
    date = models.DateField()
    certificatePDF = models.URLField()
    
    def __str__(self):
        return self.title

class Profile(models.Model):# Modelo de Perfil
    text = models.TextField()
    career = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/profile_images/')
    curriculum = models.FileField(upload_to='media/profile_pdf_curriculum/',unique=True,)
   
    def __str__(self):
        return "Profile"