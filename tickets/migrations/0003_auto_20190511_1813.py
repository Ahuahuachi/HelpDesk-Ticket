# Generated by Django 2.2.1 on 2019-05-11 18:13

from django.db import migrations


class Migration(migrations.Migration):
    atomic=False

    dependencies = [
        ('tickets', '0002_auto_20190511_1808'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Attachments',
            new_name='Attachment',
        ),
        migrations.RenameModel(
            old_name='Priorities',
            new_name='Priority',
        ),
        migrations.RenameField(
            model_name='attachment',
            old_name='attachments',
            new_name='attachment',
        ),
    ]
