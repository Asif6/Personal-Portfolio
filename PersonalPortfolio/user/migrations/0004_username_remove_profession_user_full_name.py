# Generated by Django 4.0.2 on 2022-02-07 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_skills_percentage'),
    ]

    operations = [
        migrations.CreateModel(
            name='username',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_full_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='profession',
            name='user_full_name',
        ),
    ]
