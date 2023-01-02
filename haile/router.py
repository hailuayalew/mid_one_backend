from student.viewsets import studentViewset
from rest_framework import routers


router1=routers.SimpleRouter()
router1.register('student',studentViewset)

