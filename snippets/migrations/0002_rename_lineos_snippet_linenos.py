# Generated by Django 5.0.2 on 2024-03-05 14:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='snippet',
            old_name='lineos',
            new_name='linenos',
        ),
    ]
