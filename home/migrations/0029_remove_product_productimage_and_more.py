# Generated by Django 4.1.4 on 2023-01-17 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0028_alter_product_camera_alter_product_core_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='ProductImage',
        ),
        migrations.AddField(
            model_name='productsimages',
            name='ProductImage',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='home.product'),
        ),
    ]
