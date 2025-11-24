from rest_framework import viewsets
from .models import AssignmentTransaction
from .serializers import AssignmentTransactionSerializer

class AssignmentTransactionViewSet(viewsets.ModelViewSet):
    queryset = AssignmentTransaction.objects.all()
    serializer_class = AssignmentTransactionSerializer
