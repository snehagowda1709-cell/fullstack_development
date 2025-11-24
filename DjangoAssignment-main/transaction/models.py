from django.db import models
from Basefolder.models import AbstractModel
from student.models import Student
from assignment.models import Assignment


class AssignmentTransaction(AbstractModel):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    marks = models.FloatField(null=True, blank=True)
    submitted_at = models.DateTimeField(null=True, blank=True)
