# Generated by Django 4.0.2 on 2022-02-07 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_remove_workingjourney_projectscompleted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='img',
            field=models.FileField(upload_to='media/user/Services'),
        ),
    ]