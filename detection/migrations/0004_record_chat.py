# Generated by Django 3.2.9 on 2021-12-23 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
        ('detection', '0003_record_doctor'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='chat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='chat.chat'),
        ),
    ]
