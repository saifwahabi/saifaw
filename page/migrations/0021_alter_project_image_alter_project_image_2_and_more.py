# Generated by Django 5.0.4 on 2024-07-07 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0020_project_image_2_project_image_3'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.FileField(null=True, upload_to='project/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='image_2',
            field=models.FileField(null=True, upload_to='project/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='image_3',
            field=models.FileField(null=True, upload_to='project/'),
        ),
    ]
