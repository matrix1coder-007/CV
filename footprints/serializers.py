from rest_framework import serializers

# Create your serializers here
from .models import Visits, VisitPics

class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visits
        fields = ("__all__")

class VisitPicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisitPics
        fields = ("__all__")