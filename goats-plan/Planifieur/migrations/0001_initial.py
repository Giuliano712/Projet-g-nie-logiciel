# Generated by Django 5.1.3 on 2024-11-19 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tache',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=100)),
                ('importance', models.CharField(max_length=100)),
                ('deadline', models.CharField(max_length=100)),
            ],
        ),
    ]
