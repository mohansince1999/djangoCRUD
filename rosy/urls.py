from rest_framework import routers
from rosy.views.student_view import StudentViewset
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r"student",StudentViewset)


urlpatterns= [

    path('student', include(router.urls))

]