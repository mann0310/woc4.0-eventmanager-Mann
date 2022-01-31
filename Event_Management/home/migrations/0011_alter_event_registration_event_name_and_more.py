# Generated by Django 4.0 on 2022-01-24 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_alter_participant_registration_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event_registration',
            name='event_name',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='participant_registration',
            unique_together={('select_event', 'email')},
        ),
    ]
