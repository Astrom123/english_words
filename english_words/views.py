from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.exceptions import PermissionDenied
from .serializers import *
from django.conf import settings
from django.shortcuts import get_object_or_404


def check_secret(request):
    if request.headers.get('Secret', None) != settings.API_SECRET:
        raise PermissionDenied


class WordView(APIView):
    def get(self, request, pk):
        check_secret(request)
        word = get_object_or_404(Word, id=pk)
        serializer = WordSerializer(word)
        return Response(serializer.data)


class LevelsListView(APIView):
    def get(self, request):
        check_secret(request)
        levels = Level.objects.all()
        serializer = LevelSerializer(levels, many=True)
        return Response(serializer.data)


class CategoriesListView(APIView):
    def get(self, request):
        check_secret(request)
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


class ThemesListView(APIView):
    def get(self, request):
        check_secret(request)
        themes = Theme.objects.all()
        serializer = ThemeListSerializer(themes, many=True)
        return Response(serializer.data)


class ThemeView(APIView):
    def get(self, request, pk):
        check_secret(request)
        theme = get_object_or_404(Theme, id=pk)
        serializer = ThemeSerializer(theme)
        return Response(serializer.data)
