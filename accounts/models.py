
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class StudentUserManager(BaseUserManager):
    def create_user(self, student_id, password=None):
        if not student_id:
            raise ValueError("Students must have a student ID")
        user = self.model(student_id=student_id)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, student_id, password=None):
        user = self.create_user(student_id, password)
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class StudentUser(AbstractBaseUser, PermissionsMixin):  # <-- PermissionsMixin add করো
    student_id = models.CharField(max_length=20, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)        # <-- Add this
    is_superuser = models.BooleanField(default=False)    # <-- Add this

    USERNAME_FIELD = 'student_id'
    REQUIRED_FIELDS = []

    objects = StudentUserManager()

    def __str__(self):
        return self.student_id

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser
