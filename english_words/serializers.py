from rest_framework import serializers
from .models import Word, Level, Theme, Category


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = "__all__"


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ThemeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theme
        exclude = ['words']


class WordNameIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = ['id', 'name']


class ThemeSerializer(serializers.ModelSerializer):
    words = WordNameIdSerializer(many=True)

    class Meta:
        model = Theme
        fields = "__all__"
