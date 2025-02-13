from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Category, Course
from students.models import Student
from enrollments.models import Enrollment
from .forms import CategoryForm, CourseForm
from enrollments.forms import EnrollmentForm
from students.forms import StudentForm
from django.http import HttpResponse
from .tasks import send_registration_email_to_Student
import string
import secrets
from django.core.mail import send_mail
from django.conf import settings


# Create Category
def create_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Category created successfully!")
            # return redirect("category_list")
    else:
        form = CategoryForm()

    categories = Category.objects.all()
    return render(
        request, "category_form.html", {"form": form, "categories": categories}
    )


# Create Course
def create_course(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Course created successfully!")
            # return redirect("course_list")
    else:
        form = CourseForm()

    courses = Course.objects.all()
    return render(request, "course_form.html", {"form": form, "courses": courses})


# Create Student
def create_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():

            messages.success(request, "Student created successfully!")
            # characters = string.ascii_letters + string.digits + string.punctuation
            password = "student123"
            # send_registration_email_to_Student(form.cleaned_data["email"], password)
            send_mail(
                "Welcome!",
                f"Thank you, you have been successfully registered!\n\nUsername: {form.cleaned_data["email"]}\nPassword: {password}",
                "singhnischal355@gmail.com",  # This is the 'from_email'
                [form.cleaned_data["email"]],  # This is the 'recipient_list'
                # Optional argument, set to False if you want to raise errors
            )
            form.save()
            # return redirect("student_list")
    else:
        form = StudentForm()

    students = Student.objects.all()
    return render(request, "student_form.html", {"form": form, "students": students})


# def send_registration_email_to_Student(email, password):
#     EMAIL_HOST_USER = settings.EMAIL_HOST_USER
#     send_mail(
#         "Welcome!",
#         "Thank you you have been successfully registered!",
#         f"username:{email}",
#         f"password:{password}",
#         EMAIL_HOST_USER,
#         [email],
#         fail_silently=False,
#     )


# Enroll Student
def enroll_student(request):
    if request.method == "POST":
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Student enrolled successfully!")
            # return redirect("enrollment_list")
    else:
        form = EnrollmentForm()

    enrollments = Enrollment.objects.all()
    return render(
        request, "enrollment_form.html", {"form": form, "enrollments": enrollments}
    )
