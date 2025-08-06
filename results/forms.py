
from django import forms
from add_result.models import Student


class StudentSearchForm(forms.Form):
    student_id = forms.CharField(label="Student ID", max_length=20)
    semester = forms.ChoiceField(choices=Student.SEMESTER_CHOICES, label="Semester")
