
from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student, Subject

def add_result(request):
    if request.method == 'POST':
        student_form = StudentForm(request.POST)

        if student_form.is_valid():
            student = student_form.save(commit=False)

            # Check for duplicate student ID + semester
            if Student.objects.filter(student_id=student.student_id, semester=student.semester).exists():
                student_form.add_error('student_id', 'This student ID already has results for this semester.')
            else:
                student.save()

                subjects_name = request.POST.getlist('subjects_name')
                custom_subjects = request.POST.getlist('custom_subject')
                marks_list = request.POST.getlist('marks')

                for i in range(len(subjects_name)):
                    selected_subject = subjects_name[i]
                    custom_subject = custom_subjects[i].strip() if i < len(custom_subjects) else ''
                    marks = marks_list[i] if i < len(marks_list) else None

                    # Final subject name decision
                    if selected_subject == 'Other' and custom_subject:
                        final_subject = custom_subject
                    else:
                        final_subject = selected_subject

                    # Validation check before saving
                    if final_subject and marks:
                        Subject.objects.create(
                            student=student,
                            subject_name=final_subject,
                            marks=marks
                        )

                return redirect('success')
    else:
        student_form = StudentForm()

    return render(request, 'results/add_result.html', {
        'student_form': student_form,
    })


def success(request):
    return render(request, 'results/success.html')
