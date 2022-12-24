from rest_framework.serializers import ModelSerializer
from rosy.models.student import Student

class StudentSerializer(ModelSerializer):


    class Meta:
        model=Student
        fields =(
            "id",
            "student_name",
            "email",
            "phone"
        )