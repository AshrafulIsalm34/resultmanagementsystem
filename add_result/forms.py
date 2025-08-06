
from django import forms
from .models import Student, Subject
from django.forms.models import inlineformset_factory

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_name', 'student_id', 'semester']

    def clean(self):
        cleaned_data = super().clean()
        student_id = cleaned_data.get('student_id')
        semester = cleaned_data.get('semester')

        # Only check for duplicates if both fields are valid
        if student_id and semester:
            if Student.objects.filter(student_id=student_id, semester=semester).exists():
                raise forms.ValidationError("This student ID already has results for this semester.")
        return cleaned_data


class SubjectForm(forms.ModelForm):
    SUBJECT_CHOICES = [
        ('Math', 'Math'),
        ('Logic Design', 'Logic Design'),
        ('EEE', 'EEE'),
        ('Object Oriented Programming', 'Object Oriented Programming'),
    ]

    subjects_name = forms.ChoiceField(
        choices=SUBJECT_CHOICES,
        required=True,
        label="Subject",
        widget=forms.Select(attrs={'class': 'subject-select'})
    )
    custom_subject = forms.CharField(
        required=False,
        label="Custom Subject (if Other)",
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter custom subject name',
            'class': 'custom-subject-input'
        })
    )

    class Meta:
        model = Subject
        fields = ['subjects_name', 'marks']

SubjectFormSet = inlineformset_factory(
    Student,
    Subject,
    form=SubjectForm,
    extra=3,
    can_delete=True
)
