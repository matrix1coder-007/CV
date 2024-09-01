from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Contact
from .serializers import ContactSerializer

"""
There is a need to put get and post methods in different APIViews since the audience will not be able to write on the project or post any method.
It's a static website meant for display of items for the audience. So, the post APIs are only for developer use.....
"""

class ContactGetView(APIView):
    ser_class = ContactSerializer

    def get(self, request):
        data = Contact.objects.values(
           "contact_s_num",
           "contact_type",
           "contact_link",
           "contact_downloadable"
        )
        ser = self.ser_class(data, many=True)
        return Response("The contact records have been fetched successfully:)", status=status.HTTP_200_OK)


class ContactPostView(APIView):
    ser_class = ContactSerializer

    def post(self, request):
        ser = self.ser_class(data = request.data)
        if ser.is_valid(raise_exception=True):
            ser.save()
            return Response("The contact record has been saved successfully:)", status=status.HTTP_201_CREATED)
        return Response(ser.errors)