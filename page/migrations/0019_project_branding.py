# Generated by Django 5.0.4 on 2024-07-06 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0018_rename_url_project_url_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='branding',
            field=models.TextField(max_length=30, null=True),
        ),
    ]
