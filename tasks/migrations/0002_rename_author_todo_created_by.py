# Generated by Django 4.1.2 on 2022-10-06 10:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='author',
            new_name='created_by',
        ),
    ]
