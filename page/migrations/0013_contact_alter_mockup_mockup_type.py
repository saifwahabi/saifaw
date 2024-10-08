# Generated by Django 5.0.4 on 2024-05-24 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0012_alter_mockup_background_color'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='mockup',
            name='mockup_type',
            field=models.TextField(choices=[('phone', 'phone'), ('iphone 15', 'iphone 15'), ('phone prototype', 'phone Prototype'), ('ipad', 'ipad'), ('mac pro', 'mac pro'), ('mac pro studio', 'mac pro studio'), ('prototype', 'prototype'), ('big video', 'big video'), ('big image', 'big image')], max_length=30, null=True),
        ),
    ]
