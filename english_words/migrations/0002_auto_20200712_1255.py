# Generated by Django 3.0.4 on 2020-07-12 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('english_words', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.RemoveField(
            model_name='category',
            name='code',
        ),
        migrations.RemoveField(
            model_name='level',
            name='icon',
        ),
        migrations.AddField(
            model_name='category',
            name='icon',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='level',
            name='code',
            field=models.CharField(default=1, max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='word',
            name='sound',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
    ]
