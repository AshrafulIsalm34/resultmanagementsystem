from django.urls import path
from .views import StudentSignUpView, StudentLoginView, StudentLogoutView, DashboardView

urlpatterns = [
    path('signup/', StudentSignUpView.as_view(), name='signup'),
    path('login/', StudentLoginView.as_view(), name='login'),
    path('logout/', StudentLogoutView.as_view(), name='logout'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
]
