from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import School, College
from .serializers import SchoolSerializer, CollegeSerializer

"""
There is a need to put get and post methods in different APIViews since the audience will not be able to write on the project or post any method.
It's a static website meant for display of items for the audience. So, the post APIs are only for developer use.....
"""

class SchoolGetView(APIView):
    ser_class = SchoolSerializer

    def get(self, request):
        data = School.objects.values(
            "edu_institute_s_num",
            "edu_institute_name",
            "edu_institute_address",
            "edu_institute_from",
            "edu_institute_to",
            "edu_institute_board",
            "edu_institute_website",
            "edu_downloadable",
            "school_pic",
        )
        ser = self.ser_class(data, many=True)
        # return Response("The school records have been fetched successfully:)", status=status.HTTP_200_OK)
        return Response(ser.data, status=status.HTTP_200_OK)

class SchoolPostView(APIView):
    ser_class = SchoolSerializer

    def post(self, request):
        ser = self.ser_class(data = request.data)
        if ser.is_valid(raise_exception=True):
            ser.save()
            return Response("The school record has been saved successfully:)", status=status.HTTP_201_CREATED)
        return Response(ser.errors)

class CollegeGetView(APIView):
    ser_class = CollegeSerializer

    def get(self, request):
        data = College.objects.values(
            "edu_institute_s_num",
            "edu_institute_name",
            "edu_institute_address",
            "edu_institute_from",
            "edu_institute_to",
            "edu_institute_board",
            "edu_institute_website",
            "edu_downloadable",
            "college_pic",
        )
        ser = self.ser_class(data, many=True)
        # return Response("The college records have been fetched successfully:)", status=status.HTTP_200_OK)
        return Response(ser.data, status=status.HTTP_200_OK)

class CollegePostView(APIView):
    ser_class = CollegeSerializer

    def post(self, request):
        ser = self.ser_class(data = request.data)
        if ser.is_valid(raise_exception=True):
            ser.save()
            return Response("The college record has been saved successfully:)", status=status.HTTP_201_CREATED)
        return Response(ser.errors)

