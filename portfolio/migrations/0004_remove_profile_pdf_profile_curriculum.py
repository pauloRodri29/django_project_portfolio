# Generated by Django 5.0.3 on 2024-03-23 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_profile_pdf'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='pdf',
        ),
        migrations.AddField(
            model_name='profile',
            name='curriculum',
            field=models.FileField(default='unknown', upload_to='media/profile_pdf_curriculum/'),
            preserve_default=False,
        ),
    ]
