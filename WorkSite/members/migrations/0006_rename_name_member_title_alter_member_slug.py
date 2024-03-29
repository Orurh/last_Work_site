# Generated by Django 5.0.2 on 2024-02-27 20:17

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_alter_member_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='name',
            new_name='title',
        ),
        migrations.AlterField(
            model_name='member',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, max_length=255, populate_from='name', unique=True),
        ),
    ]
