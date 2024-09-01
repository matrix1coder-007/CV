from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Visits, VisitPics
from .serializers import VisitSerializer, VisitPicsSerializer

"""
There is a need to put get and post methods in different APIViews since the audience will not be able to write on the project or post any method.
It's a static website meant for display of items for the audience. So, the post APIs are only for developer use.....
"""

class VisitGetView(APIView):
    ser_class= VisitSerializer

    def get(self, request):
        data = Visit.objects.values(
            "visit_s_num",
            "visit_destination",
            "visit_year",
            "visit_description",
        )
        ser = self.ser_class(data, many=True)
        return Response("The article records have been fetched successfully:)", status=status.HTTP_200_OK)


class VisitPostView(APIView):
    ser_class = VisitSerializer

    def post(self, request):
        ser = self.ser_class(data = request.data)
        if ser.is_valid(raise_exception=True):
            ser.save()
            return Response("The visit record has been saved successfully:)", status=status.HTTP_201_CREATED)
        return Response(ser.errors)

class VisitPicsGetView(APIView):
    ser_class = VisitPicsSerializer

    def get(self, request):
        data = VisitPics.objects.values(
           "visit_pics_s_num",
           "visit_pic_image",
           "visit_s_num"
        )
        ser = self.ser_class(data, many=True)
        return Response("The visit_pics records have been fetched successfully:)", status=status.HTTP_200_OK)


class VisitPicsPostView(APIView):
    ser_class = VisitPicsSerializer

    def post(self, request):
        ser = self.ser_class(data = request.data)
        if ser.is_valid(raise_exception=True):
            ser.save()
            return Response("The visit_pics record has been saved successfully:)", status=status.HTTP_201_CREATED)
        return Response(ser.errors)


class TaggedFootstepsGetView(APIView):
    ser_class = VisitSerializer

    def get(self, request):
        data = Article.objects.select_related("VisitPics").values(
            "visit_s_num",
            "visit_destination",
            "visit_year",
            "visit_description",
            "visit_pic_img"
        )
        ser = self.ser_class(data, many=True)
        return Response("The visit_pics have been fetched successfully:)", status=status.HTTP_200_OK)