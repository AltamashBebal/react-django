# Generated by Django 3.2.7 on 2022-01-15 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(max_length=255),
        ),
    ]
