# Generated by Django 3.2.22 on 2023-12-08 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0011_examroutine'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
