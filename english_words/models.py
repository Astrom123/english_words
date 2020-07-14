from django.db import models
from django.utils.html import mark_safe


class Word(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    translation = models.TextField()
    transcription = models.TextField()
    example = models.TextField()
    sound = models.URLField()

    def __str__(self):
        return str(self.name)

    def audio_file_player(self):
        audio_url = str(self.sound)
        player = '<audio controls="controls" > <source src="%s"/> Your browser does not support the audio ' \
                 'element.</audio> '
        return mark_safe(player % audio_url)

    audio_file_player.short_description = 'Play sound'


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    icon = models.URLField()

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return str(self.name)

    def icon_preview(self):
        icon_url = str(self.icon)
        return mark_safe('<img src="%s"/>' % icon_url)


class Level(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    code = models.CharField(max_length=2)

    def __str__(self):
        return str(self.code)


class Theme(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    level = models.ForeignKey('Level', on_delete=models.PROTECT)
    words = models.ManyToManyField(Word)
    photo = models.URLField()

    def __str__(self):
        return str(self.name)

    def photo_preview(self):
        photo_url = str(self.photo)
        return mark_safe('<img src="%s"/>' % photo_url)
