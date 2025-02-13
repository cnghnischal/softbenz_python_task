from django.contrib import admin
from .models import Category, Course, Video, Document, MCQQuestion, MCQChoice

# Register your models here.

admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Video)
admin.site.register(Document)
admin.site.register(MCQQuestion)
admin.site.register(MCQChoice)