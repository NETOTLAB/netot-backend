# Generated by Django 3.0.3 on 2020-03-09 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netot', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='retailer',
            name='bank_account',
            field=models.IntegerField(blank=True),
        ),
    ]
