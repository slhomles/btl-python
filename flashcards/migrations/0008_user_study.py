# Generated by Django 4.2.16 on 2024-11-07 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flashcards', '0007_merge_20241107_2211'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id_user', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=200)),
                ('slug_user', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Study',
            fields=[
                ('id_study', models.AutoField(primary_key=True, serialize=False)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('slug_study', models.SlugField()),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flashcards.user')),
            ],
        ),
    ]