# Generated by Django 4.2 on 2024-02-12 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='sale_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10),
        ),
    ]