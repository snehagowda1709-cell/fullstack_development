from django.contrib import admin
from .models import Course, Semester, Subject, TechSkill

admin.site.register(Course)
admin.site.register(Semester)
admin.site.register(Subject)
admin.site.register(TechSkill)
