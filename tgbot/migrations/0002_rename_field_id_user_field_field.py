# Generated by Django 5.0.4 on 2024-04-29 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tgbot', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_field',
            old_name='field_id',
            new_name='field',
        ),
    ]
