from django import forms
from .models import Category, Course, Video, Document, MCQQuestion

class CourseForm(forms.ModelForm):
    title = forms.CharField(max_length=255, required=True)
    description = forms.CharField(widget=forms.Textarea, required=True)
    price = forms.FloatField(required=True)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=True)
    video = forms.FileField(required=False)
    document = forms.FileField(required=False)

    class Meta:
        model = Course
        fields = ["title", "description", "price", "category"]

class CategoryForm(forms.ModelForm):
    title=forms.CharField(max_length=255,required=True)
    priority=forms.IntegerField(required=True)
    parent=forms.ModelChoiceField(queryset=Category.objects.all(),required=False)

    class Meta:
        model=Category
        fields=["title","priority","parent"]

class VideoForm(forms.ModelForm):
    title=forms.CharField(max_length=255,required=True)
    file=forms.FileField(required=True, widget=forms.ClearableFileInput(attrs={'accept': '.mp4'}), max_length=52428800)
    course=forms.ModelChoiceField(queryset=Course.objects.all(),required=True)

    class Meta:
        model=Video
        fields=["title","file","course"]

class DocumentForm(forms.ModelForm):
    title=forms.CharField(max_length=255,required=True)
    file=forms.FileField(required=True, widget=forms.ClearableFileInput(attrs={'accept': '.pdf'}), max_length=10485760)
    course=forms.ModelChoiceField(queryset=Course.objects.all(),required=True)

    class Meta:
        model=Document
        fields=["title","file","course"]

# class MCQQuestionForm(forms.ModelForm):
#     question=forms.CharField(max_length=255,required=True)
#     course=forms.ModelChoiceField(queryset=Course.objects.all(),required=True)

#     class Meta:
#         model=MCQQuestion
#         fields=["question","course"]

    