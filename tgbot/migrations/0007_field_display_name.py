# Generated by Django 4.2.13 on 2024-05-24 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tgbot', '0006_user_doc_pdf'),
    ]

    operations = [
        migrations.AddField(
            model_name='field',
            name='display_name',
            field=models.CharField(default=1, max_length=256),
            preserve_default=False,
        ),
    ]