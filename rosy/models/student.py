from django.db import models


class Student(models.Model):
    student_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=50)


