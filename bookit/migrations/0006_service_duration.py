# Generated by Django 5.0.6 on 2024-08-19 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookit', '0005_alter_time_slot_end_time_alter_time_slot_start_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='duration',
            field=models.IntegerField(default=60, help_text='Duration in minutes'),
            preserve_default=False,
        ),
    ]
