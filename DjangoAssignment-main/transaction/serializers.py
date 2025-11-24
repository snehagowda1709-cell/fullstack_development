from rest_framework import serializers
from .models import AssignmentTransaction

class AssignmentTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssignmentTransaction
        fields = '__all__'
