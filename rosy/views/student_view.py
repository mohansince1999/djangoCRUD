from rest_framework import viewsets
from rosy.models.student import Student
from rosy.serializers.student_serializer import StudentSerializer

class StudentViewset(viewsets.ModelViewSet):
    serializer_class=StudentSerializer
    queryset=Student.objects.all()