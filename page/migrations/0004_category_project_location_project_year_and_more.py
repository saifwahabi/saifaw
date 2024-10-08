# Generated by Django 5.0.4 on 2024-05-01 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0003_alter_project_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='location',
            field=models.TextField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='year',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(null=True, upload_to='project/'),
        ),
    ]
