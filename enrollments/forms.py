from django import forms
from .models import Enrollment
from students.models import Student
from courses.models import Course

class EnrollmentForm(forms.ModelForm):
    student=forms.ModelChoiceField(queryset=Student.objects.all(),required=True)
    course=forms.ModelChoiceField(queryset=Course.objects.all(),required=True)

    class Meta:
        model=Enrollment
        fields=["student","course"]



