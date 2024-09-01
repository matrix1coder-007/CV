from rest_framework import serializers

# Create your serializers here
from .models import Merits

class MeritSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merits
        fields = ("__all__")