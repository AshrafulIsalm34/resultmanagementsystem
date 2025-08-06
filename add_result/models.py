from django.db import models

class Student(models.Model):
    SEMESTER_CHOICES = [
        ('Spring 2025', 'Spring 2025'),
        ('Summer 2025', 'Summer 2025'),
        ('Fall 2025', 'Fall 2025'),
        ('Spring 2024', 'Spring 2024'),
        ('Summer 2024', 'Summer 2024'),
        ('Spring 2026', 'Spring 2026'),
        ('Summer 2026', 'Summer 2026'),
        ('Fall 2026', 'Fall 2026'),
    ]

    student_name = models.CharField(max_length=100)
    student_id = models.IntegerField()
    semester = models.CharField(max_length=20, choices=SEMESTER_CHOICES) 

    def __str__(self):
        return f"{self.student_name} ({self.student_id})"
    
    class Meta:
            unique_together = ('student_id', 'semester')


class Subject(models.Model):
    student = models.ForeignKey(Student, related_name='subjects', on_delete=models.CASCADE)
    subject_name = models.CharField(max_length=50)
    marks = models.IntegerField()

    def __str__(self):
        return f"{self.subject_name} - {self.marks}"
