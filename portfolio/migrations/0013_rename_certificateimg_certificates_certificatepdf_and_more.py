# Generated by Django 5.0.3 on 2024-06-23 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0012_remove_certificates_certificatepdf_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='certificates',
            old_name='certificateIMG',
            new_name='certificatePDF',
        ),
        migrations.AlterField(
            model_name='profile',
            name='curriculum',
            field=models.FileField(unique=True, upload_to='media/profile_pdf_curriculum/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(upload_to='media/profile_images/'),
        ),
    ]
