# Generated by Django 5.0.4 on 2024-07-08 23:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0022_rename_about_3_site_data_about_2_title_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='site_data',
            old_name='middel_name',
            new_name='middle_name',
        ),
    ]
