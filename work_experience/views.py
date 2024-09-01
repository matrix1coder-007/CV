from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import WorkExp
from .serializers import WorkSerializer

"""
There is a need to put get and post methods in different APIViews since the audience will not be able to write on the project or post any method.
It's a static website meant for display of items for the audience. So, the post APIs are only for developer use.....
"""

class WorkExpGetView(APIView):
    ser_class = WorkSerializer

    def get(self, request):
        data = WorkExp.objects.values(
            "workexp_s_num",
            "workexp_type",
            "workexp_organization",
            "workexp_location",
            "workexp_industry",
            "workexp_from",
            "workexp_to",
            "workexp_downloadable",
        )
        ser = self.ser_class(data, many=True)
        # return Response("The work_exp records have been fetched successfully:)", status=status.HTTP_200_OK)
        return Response(ser.data, status=status.HTTP_200_OK)

class WorkExpPostView(APIView):
    ser_class = WorkSerializer

    def post(self, request):
        ser = self.ser_class(data = request.data)
        if ser.is_valid(raise_exception=True):
            ser.save()
            return Response("The work_exp record has been saved successfully:)", status=status.HTTP_201_CREATED)
        return Response(ser.errors)