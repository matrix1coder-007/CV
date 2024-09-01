from rest_framework import serializers

# Create your serializers here
from .models import School, College

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ("__all__")

class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = College
        fields = ("__all__")
        