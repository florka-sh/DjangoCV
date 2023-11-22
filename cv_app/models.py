
from django.db import models

class Education(models.Model):
    degree = models.CharField(max_length=100)
    institution = models.CharField(max_length=200)
    graduation_year = models.IntegerField()
    diploma = models.FileField(upload_to='diplomas/', blank=True, null=True)

class Experience(models.Model):
    job_title = models.CharField(max_length=100)
    company = models.CharField(max_length=200)
    start_year = models.IntegerField()
    end_year = models.IntegerField(null=True, blank=True)
    responsibilities = models.TextField()
    reference_letter = models.FileField(upload_to='references/', blank=True, null=True)

class Skill(models.Model):
    name = models.CharField(max_length=50)
    proficiency = models.CharField(max_length=20)


