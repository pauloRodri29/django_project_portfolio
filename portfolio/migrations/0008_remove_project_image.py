# Generated by Django 5.0.3 on 2024-03-23 19:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_remove_skillandknowledge_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='image',
        ),
    ]
