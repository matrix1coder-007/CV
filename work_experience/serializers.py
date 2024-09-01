from rest_framework import serializers

# Create your serializers here.
from .models import WorkExp

class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkExp
        fields = ("__all__")
