# Generated by Django 4.0 on 2022-01-09 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_event_registration_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant_registration',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
