# Generated by Django 5.0.2 on 2024-02-27 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0008_rename_title_member_name_alter_member_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='is_public',
            field=models.BooleanField(choices=[(0, 'Черновик'), (1, 'Опубликовано')], default=0),
        ),
    ]
