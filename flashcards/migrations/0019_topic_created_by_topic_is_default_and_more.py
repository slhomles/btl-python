# Generated by Django 4.2.16 on 2024-11-20 02:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('flashcards', '0018_alter_study_id_user_delete_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='topic',
            name='is_default',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='topic',
            name='type_topic',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
