# Generated by Django 3.2.7 on 2022-01-02 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area_name',
            name='area',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='area_name',
            name='city',
            field=models.CharField(max_length=50),
        ),
    ]
