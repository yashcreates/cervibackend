# Generated by Django 3.2.9 on 2021-12-14 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_alter_patient_phonenumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='disabled',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='patient',
            name='disabled',
            field=models.BooleanField(default=False),
        ),
    ]
