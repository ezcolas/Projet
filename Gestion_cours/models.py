import datetime
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

"""Table professeur"""

class Professeur(models.Model):
    user = models.OneToOneField(User)
    code=models.CharField(max_length=5)
    TITRE = (('Mr', 'Monsieur'), ('Mme', 'Madame'))
    titre = models.CharField(max_length=3, choices = TITRE)
    Nom = models.CharField(max_length=50)
    Domaine = models.CharField(max_length=25)
    GRADE = (('Dr', 'Doctorat'), ('Mtre', 'Maitrise'), ('BS', 'Licence'))
    Niveau = models.CharField(max_length=5, choices = GRADE)    
    email= models.EmailField()
    phone= models.CharField(max_length=15)   
    cv = models.FileField(upload_to="cv/")

    def __unicode__(self):
        return '%s'%( self.Nom)

"""Etablissement"""
class Etablissement(models.Model):
    Description = models.CharField(max_length=250)
    Abreviation = models.CharField(max_length=5)
    Adresse = models.CharField(max_length=25)
    Website = models.CharField(max_length=25)
    def __unicode__(self):
        return self.Abreviation
    
"""Table des cours"""
class cour(models.Model):
    Etablissement = models.ForeignKey(Etablissement)
    titre =  models.CharField(max_length=25)    
    GRADE = (('D1', 'DUT 1'), ('D2', 'Dut 2'), ('L1', 'Licence 1'), ('L2', 'Licence 2'), ('L3', 'Licence 3'), ('M1', 'Master 1'), ('M2', 'Master 2'))
    grade = models.CharField(max_length=2, choices = GRADE)
    SEMESTRE = (('S1', 'Semestre 1'), ('S2', 'Semestre 2'), ('Y','Annuel'))
    semestre= models.CharField(max_length=2, choices = SEMESTRE)   
    
    def __unicode__(self):
        return '%s-%s%s-%s' %(self.Etablissement,self.grade, self.semestre,self.titre)

""" Table Cours Specialise"""
class cours_specialise(models.Model):
    cour = models.ForeignKey(cour)
    DOMAINE = (('ST', 'Sciences et Technologie'), ('E&G', 'Economie et Gestion'))
    domaine = models.CharField(max_length=3, choices = DOMAINE)
    MENTION = (('SI', 'Sciences Informatiques'), ('E&G', 'Economie et Gestion'))
    mention =models.CharField(max_length=13, choices = MENTION)
    SPECIALITE = (('TEL', 'Telecomunication'), ('BDD', 'Base de donnee'), ('ONE', 'Organisation de la Net Economie'), ('SdE', 'Sciences de lentreprise'), ('SC','Sciences Comptables'))
    specialite = models.CharField(max_length=3, choices = SPECIALITE)
    TYPE_COURS =(('OB', 'Obligatoire'), ('OP', 'Optionnel'))
    type_cours = models.CharField(max_length=2, choices = TYPE_COURS)
    LANGUE = (('A', 'Anglais'), ('F', 'Francais'))
    langue = models.CharField(max_length=1, choices = LANGUE)

    def __unicode__(self):
        return '%s-%s-%s-%s-%s' %(self.domaine,self.mention, self.specialite,self.type_cours, self.langue)


"""Table Enregistremenet cours"""
class description_cour(models.Model):
    cour = models.ForeignKey(cour)
    titre = models.CharField(max_length=25)
    credit = models.CharField(max_length=15)
    lieu = models.ForeignKey(Etablissement)
    Professeur = models.ForeignKey(Professeur)
    public_cible = models.CharField(max_length=50)
    prerequis = models.CharField(max_length=50)
    objectif = models.TextField(null=True)
    description = models.TextField(null=True)
    plan_cours =models.TextField(null=True)
    format_cours = models.CharField(max_length=50)
    ressource = models.TextField(null=True)
    evaluation = models.TextField(null=True)


# Create your models here.
