# Generated by Django 5.0.4 on 2024-04-21 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_tariffoption_remove_subscription_remaining_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tariff',
            name='options',
        ),
        migrations.RemoveField(
            model_name='subscription',
            name='options',
        ),
        migrations.AddField(
            model_name='tariff',
            name='adverts_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tariff',
            name='duration',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='TariffOption',
        ),
    ]
