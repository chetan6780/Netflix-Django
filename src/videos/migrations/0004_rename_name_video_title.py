# Generated by Django 3.2.6 on 2021-08-19 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0003_auto_20210819_2210'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='name',
            new_name='title',
        ),
    ]