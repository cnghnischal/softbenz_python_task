from django.db import models
from students.models import Student
from courses.models import Course

# Create your models here.
class Enrollment(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE,related_name='enrollments')
    course=models.ForeignKey(Course,on_delete=models.CASCADE,related_name='enrollments')
    enrolled_on=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.student.name} - {self.course.title}"
    
    