# Generated by Django 4.0.2 on 2022-02-07 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_workingjourney_cup_of_coffee_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skills',
            name='percentage',
            field=models.IntegerField(),
        ),
    ]
