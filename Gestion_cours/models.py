import datetime
from django.utils import timezone
from django.db import models

"""Table professeur"""

class Professeur(models.Model):
    code=models.CharField(max_length=10)
    TITRE = (('Mr', 'Mr'), ('', 'Mme'))
    titre = models.CharField(max_length=1, choices = TITRE)
    Nom = models.CharField(max_length=25)
    Prenom = models.CharField(max_length=25)
    Matiere_enseigne = models.CharField(max_length=25)
    phone= models.CharField(max_length=15)    
    #cv = models.ImageField(upload_to='cars')
    #FileField.upload_to

    def __unicode__(self):
        return self.prenom

"""Etablissement"""
class Etablissement(models.Model):
    Description = models.CharField(max_length=250)
    Abreviation = models.CharField(max_length=5)
    
"""Table des cours"""
class cour(models.Model):
    Etablissement = models.ForeignKey(Etablissement)
    titre =  models.CharField(max_length=25)
    etablissement = models.CharField(max_length=25)
    GRADE = (('D1', 'DUT 1'), ('D2', 'Dut 2'), ('L1', 'Licence 1'), ('L2', 'Licence 2'), ('L3', 'Licence 3'), ('M1', 'Master 1'), ('M2', 'Master 2'))
    grade = models.CharField(max_length=2, choices = GRADE)
    SEMESTRE = (('S1', 'Semestre 1'), ('S2', 'Semestre 2'), ('Y','Annuel'))
    semestre= models.CharField(max_length=2, choices = SEMESTRE)

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

"""Table Enregistremenet cours"""
class description_cour(models.Model):
    cour = models.ForeignKey(cour)
    titre = models.CharField(max_length=15)
    credit = models.CharField(max_length=15)
    lieu_enseignement = models.CharField(max_length=15)
    Professeur = models.ForeignKey(Professeur)
    public_cible = models.CharField(max_length=15)
    prerequis = models.CharField(max_length=15)
    objectif = models.CharField(max_length=15)
    description = models.CharField(max_length=15)
    plan_cours =models.CharField(max_length=15)
    format_cours = models.CharField(max_length=15)
    ressource = models.CharField(max_length=15)
    evaluation = models.CharField(max_length=15)


# Create your models here.
