# from django import forms
# from django.contrib.auth.forms import AuthenticationForm
# from .models import StudentUser

# class SignUpForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)

#     class Meta:
#         model = StudentUser
#         fields = ['student_id', 'password']

# class LoginForm(AuthenticationForm):
#     username = forms.CharField(label="Student ID")
#     password = forms.CharField(widget=forms.PasswordInput)



from django import forms
from .models import StudentUser
from django.contrib.auth.forms import ReadOnlyPasswordHashField

# Signup Form
class StudentUserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = StudentUser
        fields = ('student_id',)

    def clean_password2(self):
        p1 = self.cleaned_data.get("password1")
        p2 = self.cleaned_data.get("password2")
        if p1 and p2 and p1 != p2:
            raise forms.ValidationError("Passwords don't match")
        return p2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

# Login Form
class StudentLoginForm(forms.Form):
    student_id = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
