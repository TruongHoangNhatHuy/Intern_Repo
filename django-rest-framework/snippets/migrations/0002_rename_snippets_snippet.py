# Generated by Django 5.1.2 on 2024-10-30 08:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Snippets',
            new_name='Snippet',
        ),
    ]
