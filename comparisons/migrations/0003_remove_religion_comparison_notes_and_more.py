# Generated by Django 5.1.6 on 2025-02-26 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comparisons', '0002_religion_facebook_link_religion_youtube_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='religion',
            name='comparison_notes',
        ),
        migrations.RemoveField(
            model_name='religion',
            name='principles',
        ),
    ]
