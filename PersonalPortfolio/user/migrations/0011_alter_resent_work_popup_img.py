# Generated by Django 4.0.2 on 2022-02-10 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_resent_work'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resent_work',
            name='popup_img',
            field=models.ImageField(upload_to='media/work/popup_thumbnail'),
        ),
    ]
