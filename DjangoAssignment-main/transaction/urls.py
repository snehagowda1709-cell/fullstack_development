from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AssignmentTransactionViewSet

router = DefaultRouter()
router.register('transactions', AssignmentTransactionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
