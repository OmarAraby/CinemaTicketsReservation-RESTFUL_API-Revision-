# Generated by Django 3.2.25 on 2024-04-21 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='movie',
            field=models.CharField(max_length=20),
        ),
    ]
