from django.urls import path
from .views import StudentSearchView

urlpatterns = [
    path('rs/', StudentSearchView.as_view(), name='student_search'),
]
