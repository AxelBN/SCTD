# Generated by Django 4.1.3 on 2022-11-29 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tracking', '0002_site_alter_trackdocument_site'),
    ]

    operations = [
        migrations.AddField(
            model_name='trackdocument',
            name='foto',
            field=models.FileField(blank=True, max_length=254, null=True, upload_to='', verbose_name='Foto'),
        ),
    ]
