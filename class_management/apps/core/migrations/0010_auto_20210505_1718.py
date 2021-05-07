# Generated by Django 3.1.7 on 2021-05-05 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210505_1718'),
        ('core', '0009_auto_20210505_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseinstructors',
            name='batch',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.batch'),
        ),
        migrations.AlterField(
            model_name='courseinstructors',
            name='end',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Batch',
        ),
    ]
