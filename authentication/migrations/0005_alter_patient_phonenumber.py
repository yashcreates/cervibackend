# Generated by Django 3.2.9 on 2021-12-13 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_doctor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='phoneNumber',
            field=models.CharField(max_length=11, unique=True),
        ),
    ]