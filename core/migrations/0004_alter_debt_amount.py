# Generated by Django 5.0.6 on 2024-06-15 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_debt_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='debt',
            name='amount',
            field=models.FloatField(),
        ),
    ]
