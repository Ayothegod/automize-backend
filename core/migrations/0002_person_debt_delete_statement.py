# Generated by Django 5.0.6 on 2024-06-15 07:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Debt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('CR', 'Creditor'), ('DR', 'Debtor')], max_length=255)),
                ('amount', models.IntegerField()),
                ('currency', models.CharField(max_length=4)),
                ('due_date', models.DateTimeField()),
                ('interest_rate', models.FloatField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('payment_frequency', models.CharField(choices=[('MONTHLY', 'Monthly'), ('BI-MONTHLY', 'Bi-Monthly'), ('WEEKLY', 'Weekly'), ('BI-WEEKLyY', 'Bi-Weekly'), ('QUARTERLY', 'Quarterly'), ('SEMI-ANNUALLY', 'Semi-Annually'), ('ANNUALLY', 'Annually')], max_length=20)),
                ('payment_method', models.CharField(choices=[('BANK TRANSFER', 'Bank Transfer'), ('CASH', 'Cash'), ('CREDIT CARD', 'Credit Card'), ('DEBIT CARD', 'Debit Card'), ('CHECK', 'Check'), ('OTHERS', 'Others')], max_length=50)),
                ('is_paid', models.BooleanField(default=False)),
                ('is_bad_debt', models.BooleanField(default=False)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.person')),
            ],
        ),
        migrations.DeleteModel(
            name='Statement',
        ),
    ]