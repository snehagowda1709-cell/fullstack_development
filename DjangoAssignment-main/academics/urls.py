from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, SemesterViewSet, SubjectViewSet, TechSkillViewSet

router = DefaultRouter()
router.register('courses', CourseViewSet)
router.register('semesters', SemesterViewSet)
router.register('subjects', SubjectViewSet)
router.register('techskills', TechSkillViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

