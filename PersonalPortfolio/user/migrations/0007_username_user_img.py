# Generated by Django 4.0.2 on 2022-02-07 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_alter_services_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='username',
            name='user_img',
            field=models.FileField(default='NONE', upload_to='media/user/user_img'),
        ),
    ]
