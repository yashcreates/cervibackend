# Generated by Django 3.2.9 on 2021-12-14 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0007_auto_20211214_2111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='phoneNumber',
            field=models.CharField(max_length=11, unique=True),
        ),
    ]