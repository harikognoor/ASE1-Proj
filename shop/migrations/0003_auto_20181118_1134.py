# Generated by Django 2.1.2 on 2018-11-18 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20181118_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(db_index=True, max_length=150, unique=True),
        ),
    ]