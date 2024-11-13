# Generated by Django 4.2.16 on 2024-11-13 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flashcards', '0009_flashcards_pronunciation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flashcards',
            name='pronunciation',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='flashcards',
            name='slug_flashcard',
            field=models.SlugField(),
        ),
    ]