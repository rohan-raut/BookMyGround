# Generated by Django 3.2.7 on 2022-02-24 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0005_ground_registration_ground_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='ground_id',
            field=models.CharField(default='', max_length=50),
        ),
    ]