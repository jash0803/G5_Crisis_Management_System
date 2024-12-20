# Generated by Django 5.1.2 on 2024-11-19 08:07

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0004_alter_volunteer_organization'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('taskID', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('U', 'Unsolved'), ('I', 'In Progress'), ('S', 'Solved')], max_length=1)),
                ('assignee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='management.volunteer')),
            ],
        ),
    ]
