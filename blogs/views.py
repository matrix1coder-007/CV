from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Article, Tag
from .serializers import ArticleSerializer, TagSerializer

"""
There is a need to put get and post methods in different APIViews since the audience will not be able to write on the project or post any method.
It's a static website meant for display of items for the audience. So, the post APIs are only for developer use.....
"""

class ArticleGetView(APIView):
    ser_class = ArticleSerializer

    def get(self, request):
        data = Article.objects.values(
           "article_s_num",
           "article_title",
           "article_text",
           "article_record_created",
        )
        ser = self.ser_class(data, many=True)
        return Response("The article records have been fetched successfully:)", status=status.HTTP_200_OK)


class ArticlePostView(APIView):
    ser_class = ArticleSerializer

    def post(self, request):
        ser = self.ser_class(data = request.data)
        if ser.is_valid(raise_exception=True):
            ser.save()
            return Response("The article record has been saved successfully:)", status=status.HTTP_201_CREATED)
        return Response(ser.errors)

class TagGetView(APIView):
    ser_class = TagSerializer

    def get(self, request):
        data = Tag.objects.values(
           "tag_s_num",
           "tag_title"
        )
        ser = self.ser_class(data, many=True)
        return Response("The tag records have been fetched successfully:)", status=status.HTTP_200_OK)


class TagPostView(APIView):
    ser_class = TagSerializer

    def post(self, request):
        ser = self.ser_class(data = request.data)
        if ser.is_valid(raise_exception=True):
            ser.save()
            return Response("The tag record has been saved successfully:)", status=status.HTTP_201_CREATED)
        return Response(ser.errors)


class TaggedArticleGetView(APIView):
    ser_class = ArticleSerializer

    def get(self, request):
        data = Article.objects.select_related("Tags").values(
            "article_s_num",
            "article_title",
            "article_text",
            "article_record_created"
        )
        ser = self.ser_class(data, many=True)
        return Response("The tagged articles have been fetched successfully:)", status=status.HTTP_200_OK)