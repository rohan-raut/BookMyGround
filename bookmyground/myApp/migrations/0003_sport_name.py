# Generated by Django 3.2.7 on 2022-01-02 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0002_auto_20220102_2350'),
    ]

    operations = [
        migrations.CreateModel(
            name='sport_name',
            fields=[
                ('sport_ground', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
    ]
