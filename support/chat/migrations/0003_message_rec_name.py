# Generated by Django 2.1.3 on 2018-11-12 13:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_message_roomname'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='rec_name',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
