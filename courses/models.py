from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=255)
    priority = models.IntegerField()
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title


class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField(
        validators=[
            MinValueValidator(1000.0),  # Minimum price must be 1000.0
            MaxValueValidator(99999.99),  # Maximum price allowed is 99999.99
        ]
    )
    video = models.FileField(upload_to="videos/", null=True)
    document = models.FileField(upload_to="documents/", null=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="courses"
    )
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Video(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="videos")
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to="videos/")

    def __str__(self):
        return self.title


def get_document_path(instance, filename):
    return f"documents/{instance.course.title}/{filename}"


class Document(models.Model):
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="documents"
    )
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to=get_document_path)

    def __str__(self):
        return self.title


class MCQQuestion(models.Model):
    question = models.TextField()

    def __str__(self):
        return self.question


class MCQChoice(models.Model):
    choices = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)
    question = models.ForeignKey(
        MCQQuestion, on_delete=models.CASCADE, related_name="mcqchoices"
    )
