from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Project
from .serializers import ProjectSerializer

"""
There is a need to put get and post methods in different APIViews since the audience will not be able to write on the project or post any method.
It's a static website meant for display of items for the audience. So, the post APIs are only for developer use.....
"""

class ProjectGetView(APIView):
    ser_class = ProjectSerializer

    def get(self, request):
        data = Project.objects.values(
           "project_s_num",
           "project_title",
           "project_abstract",
           "project_type",
           "project_organization",
           "project_nature",
           "project_from",
           "project_to",
           "project_downloadable"
        )
        ser = self.ser_class(data, many=True)
        return Response("The project records have been fetched successfully:)", status=status.HTTP_200_OK)


class ProjectPostView(APIView):
    ser_class = ProjectSerializer

    def post(self, request):
        ser = self.ser_class(data = request.data)
        if ser.is_valid(raise_exception=True):
            ser.save()
            return Response("The project record has been saved successfully:)", status=status.HTTP_201_CREATED)
        return Response(ser.errors)