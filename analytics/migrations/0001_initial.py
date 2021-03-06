# Generated by Django 2.2 on 2019-05-12 18:54

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('project', '0003_project_ips'),
    ]

    operations = [
        migrations.CreateModel(
            name='Analytics',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('data', models.TextField(editable=False)),
                ('ip', models.CharField(editable=False, max_length=200)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Project')),
            ],
        ),
    ]
