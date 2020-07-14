from django.contrib import admin
from django.forms import Textarea

from .models import Word, Level, Theme, Category
from django.db import models


@admin.register(Word)
class WordAdmin(admin.sites.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 1, 'cols': 100})},
    }
    readonly_fields = ['audio_file_player']


@admin.register(Level)
class LevelAdmin(admin.sites.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 1, 'cols': 40})},
        models.CharField: {'widget': Textarea(attrs={'rows': 1, 'cols': 40})},
    }


@admin.register(Category)
class CategoryAdmin(admin.sites.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 1, 'cols': 40})},
    }
    readonly_fields = ['icon_preview']


@admin.register(Theme)
class ThemeAdmin(admin.sites.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 1, 'cols': 40})},
    }
    readonly_fields = ['photo_preview']
