from django.contrib import admin
from .models import Student, Subject

class SubjectInline(admin.TabularInline):
    model = Subject
    extra = 1

class StudentAdmin(admin.ModelAdmin):
    inlines = [SubjectInline]
    list_display = ('student_name', 'student_id', 'semester')

admin.site.register(Student, StudentAdmin)


