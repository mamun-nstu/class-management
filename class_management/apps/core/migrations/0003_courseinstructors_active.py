# Generated by Django 3.1.7 on 2021-05-05 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210505_1647'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseinstructors',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]