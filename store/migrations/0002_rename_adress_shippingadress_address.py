# Generated by Django 4.0.3 on 2022-08-01 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shippingadress',
            old_name='adress',
            new_name='address',
        ),
    ]
