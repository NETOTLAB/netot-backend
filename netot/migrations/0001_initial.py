# Generated by Django 3.0.3 on 2020-03-09 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_id', models.CharField(max_length=20, unique=True)),
                ('location', models.CharField(max_length=10)),
                ('gas_flow', models.FloatField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('cylinder_type', models.CharField(choices=[('6kg', '6kg'), ('12kg', '12kg'), ('15kg', '15kg'), ('18kg', '18kg'), ('20kg', '20kg')], default='6kg', max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Retailer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('owner_name', models.CharField(max_length=30)),
                ('tin_number', models.IntegerField()),
                ('location', models.CharField(max_length=10)),
                ('bank', models.CharField(choices=[('EQuityBank', 'Equity Bank'), ('CogeBanque', 'CogeBanque'), ('BK', 'Bank of Kigali'), ('GT', 'GT Bank'), ('KCB', 'KCB')], max_length=20)),
                ('bank_account', models.IntegerField(blank=True, max_length=20)),
                ('gas_importer', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Household',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=20)),
                ('lname', models.CharField(max_length=20)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('phone_number', models.CharField(max_length=10)),
                ('bank', models.CharField(blank=True, choices=[('EQuityBank', 'Equity Bank'), ('CogeBanque', 'CogeBanque'), ('BK', 'Bank of Kigali'), ('GT', 'GT Bank'), ('KCB', 'KCB')], max_length=20)),
                ('bank_account', models.IntegerField(blank=True)),
                ('gaz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='netot.Gas')),
            ],
        ),
    ]
