# Generated by Django 4.2.16 on 2024-10-15 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flashcards', '0002_alter_topic_id_topic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flashcards',
            name='id_flashcard',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]