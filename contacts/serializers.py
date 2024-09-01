from rest_framework import serializers

# Create your serializers here
from .models import Contact

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ("__all__")