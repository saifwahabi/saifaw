# Generated by Django 5.0.4 on 2024-07-09 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0023_rename_middel_name_site_data_middle_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='mockup',
            name='order',
            field=models.IntegerField(null=True),
        ),
    ]
