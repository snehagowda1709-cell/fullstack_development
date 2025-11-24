from django.db import models
from org.models import Organization

class Semester(models.Model):
    name = models.CharField(max_length=64)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=128)
    code = models.CharField(max_length=32, unique=True, default="DEFAULT_CODE")  # default added!
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, related_name='subjects')

    def __str__(self):
        return self.name

class TechSkill(models.Model):
    name = models.CharField(max_length=128)
    proficiency = models.CharField(max_length=32, blank=True)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    course_code = models.CharField(max_length=32, default="DEFAULT_CODE")
    submission_end = models.DateField(null=True, blank=True)
    semester = models.ForeignKey(Semester, on_delete=models.SET_NULL, null=True, blank=True)
    subjects = models.ManyToManyField(Subject, blank=True)
    tech_skills = models.ManyToManyField(TechSkill, blank=True)

    def __str__(self):
        return self.name
