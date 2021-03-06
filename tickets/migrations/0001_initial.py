# Generated by Django 2.2.1 on 2019-05-11 18:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Attachments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attachments', models.URLField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Priorities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priority', models.CharField(choices=[('LO', 'Low'), ('HI', 'High'), ('UR', 'Urgent')], default='LO', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('OP', 'Open'), ('PE', 'Pending'), ('RE', 'Resolved'), ('CL', 'Closed')], default='OP', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('fk_agent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('fk_attachments', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tickets.Attachments')),
                ('fk_priority', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tickets.Priorities')),
                ('fk_requester', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('fk_status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tickets.Status')),
            ],
        ),
    ]
