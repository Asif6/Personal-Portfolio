# Generated by Django 4.0.2 on 2022-02-07 19:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_username_remove_profession_user_full_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workingjourney',
            name='ProjectsCompleted',
        ),
    ]
