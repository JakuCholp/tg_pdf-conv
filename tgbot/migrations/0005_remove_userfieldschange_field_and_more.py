# Generated by Django 5.0.4 on 2024-05-01 08:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tgbot', '0004_userfieldschange_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userfieldschange',
            name='field',
        ),
        migrations.AddField(
            model_name='userfieldschange',
            name='user_field',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tgbot.user_field'),
        ),
    ]
