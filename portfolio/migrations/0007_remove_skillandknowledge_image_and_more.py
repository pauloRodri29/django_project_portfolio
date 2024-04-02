# Generated by Django 5.0.3 on 2024-03-23 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_certificates_skillandknowledge_delete_knowledge_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skillandknowledge',
            name='image',
        ),
        migrations.AddField(
            model_name='skillandknowledge',
            name='imageURL',
            field=models.URLField(default='unknown'),
            preserve_default=False,
        ),
    ]
