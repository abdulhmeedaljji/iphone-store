# Generated by Django 3.2.6 on 2021-08-30 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_land'),
    ]

    operations = [
        migrations.AddField(
            model_name='disease',
            name='diseaseImage',
            field=models.ImageField(default=1, upload_to='diseases'),
            preserve_default=False,
        ),
    ]
