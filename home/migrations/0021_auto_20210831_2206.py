# Generated by Django 3.2.6 on 2021-08-31 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_alter_product_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='trancation_id',
            new_name='transaction_id',
        ),
        migrations.RemoveField(
            model_name='shippingadderss',
            name='adders',
        ),
        migrations.RemoveField(
            model_name='shippingadderss',
            name='stats',
        ),
        migrations.AddField(
            model_name='shippingadderss',
            name='address',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='shippingadderss',
            name='state',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='shippingadderss',
            name='zipcode',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='shippingadderss',
            name='city',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
