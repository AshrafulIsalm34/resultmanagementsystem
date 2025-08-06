from django.shortcuts import render
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.views import View
from .forms import StudentSearchForm
from add_result.models import Student


# Base View (Abstraction)
class BaseStudentSearchView(View):
    form_class = StudentSearchForm
    template_name = 'results/result.html'

    def get_context_data(self):
        return {'form': self.form_class()}

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())


# Utility for GPA Calculation (Encapsulation)
class GPACalculator:
    @staticmethod
    def get_gpa(marks):
        if marks >= 80:
            return 4.00
        elif marks >= 70:
            return 3.50
        elif marks >= 60:
            return 3.00
        elif marks >= 50:
            return 2.50
        elif marks >= 40:
            return 2.00
        else:
            return 0.00

    @classmethod
    def calculate_subject_gpas(cls, subjects):
        return [cls.get_gpa(subject.marks) for subject in subjects]

    @classmethod
    def calculate_gpa(cls, subjects):
        gpas = cls.calculate_subject_gpas(subjects)
        if gpas:
            return round(sum(gpas) / len(gpas), 2)
        return 0.00


# Inherited + Polymorphic View
class StudentSearchView(BaseStudentSearchView):
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            student_id = form.cleaned_data['student_id']
            semester = form.cleaned_data['semester']
            student = Student.objects.filter(student_id=student_id, semester=semester).first()

            if student:
                subjects = student.subjects.all()
                semester_gpa = GPACalculator.calculate_gpa(subjects)

                # Get all semesters for this student ID
                all_semesters = Student.objects.filter(student_id=student_id)
                all_gpas = [GPACalculator.calculate_gpa(s.subjects.all()) for s in all_semesters if s.subjects.exists()]
                cgpa = round(sum(all_gpas) / len(all_gpas), 2) if all_gpas else 0.0

                html = render_to_string('partials/student_card.html', {
                    'student': student,
                    'subjects': subjects,
                    'semester_gpa': semester_gpa,
                    'cgpa': cgpa
                })
                return JsonResponse({'status': 'success', 'card_html': html})
            else:
                return JsonResponse({'status': 'error', 'message': 'No student found'})
        return JsonResponse({'status': 'error', 'message': 'Invalid form'})
