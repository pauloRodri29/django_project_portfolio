# Generated by Django 5.0.3 on 2024-03-23 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_profile_career'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='pdf',
            field=models.FileField(default='unknown', upload_to='media/profile_pdfs/'),
            preserve_default=False,
        ),
    ]
