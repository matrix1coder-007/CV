from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Merits
from .serializers import MeritSerializer

"""
There is a need to put get and post methods in different APIViews since the audience will not be able to write on the project or post any method.
It's a static website meant for display of items for the audience. So, the post APIs are only for developer use.....
"""

class MeritGetView(APIView):
    ser_class = MeritSerializer

    def get(self, request):
        data = Merit.objects.values(
           "merit_s_num",
           "merit_type",
           "merit_title",
           "merit_year",
           "merit_rank",
           "merit_description",
           "merit_organization",
           "merit_downloadable"
        )
        ser = self.ser_class(data, many=True)
        return Response("The merit records have been fetched successfully:)", status=status.HTTP_200_OK)


class MeritPostView(APIView):
    ser_class = MeritSerializer

    def post(self, request):
        ser = self.ser_class(data = request.data)
        if ser.is_valid(raise_exception=True):
            ser.save()
            return Response("The contact record has been saved successfully:)", status=status.HTTP_201_CREATED)
        return Response(ser.errors)