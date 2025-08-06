
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, TemplateView, FormView, RedirectView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import StudentUser
from .forms import StudentUserCreationForm, StudentLoginForm

# Signup View
class StudentSignUpView(FormView):
    template_name = 'accounts/signup.html'
    form_class = StudentUserCreationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

# Login View
class StudentLoginView(FormView):
    template_name = 'accounts/login.html'
    form_class = StudentLoginForm
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        student_id = form.cleaned_data.get('student_id')
        password = form.cleaned_data.get('password')
        user = authenticate(self.request, student_id=student_id, password=password)
        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        return self.form_invalid(form)

# Logout View
class StudentLogoutView(RedirectView):
    url = reverse_lazy('login')

    def get(self, request, *args, **kwargs):
        logout(request)
        return super().get(request, *args, **kwargs)

# Dashboard View (Login Required)
class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/dashboard.html'

    login_url = reverse_lazy('login')

