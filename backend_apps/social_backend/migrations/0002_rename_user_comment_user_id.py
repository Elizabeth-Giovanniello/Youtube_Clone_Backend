# Generated by Django 4.0.2 on 2022-02-22 21:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social_backend', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='user',
            new_name='user_id',
        ),
    ]
