from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    name=forms.CharField(max_length=255,required=True)
    email=forms.EmailField(required=True)

    class Meta:
        model=Student
        fields=["name","email"]