# Generated by Django 3.1.7 on 2022-03-05 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('core', '0005_auto_20210828_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='instructors',
            field=models.ManyToManyField(blank=True, null=True, related_name='courses', through='core.CourseInstructors', to='users.Instructor'),
        ),
    ]
