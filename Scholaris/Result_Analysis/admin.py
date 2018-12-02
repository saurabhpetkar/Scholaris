from django.contrib import admin
from .models import Student, Teacher, Course, Task

# Register your models here.

admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Task)