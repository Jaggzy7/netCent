# Generated by Django 4.0.3 on 2022-03-03 10:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Business', '0003_rename_inventor_inventory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inventory',
            old_name='last_dales_date',
            new_name='last_sales_date',
        ),
    ]
