# Generated by Django 5.0.4 on 2024-04-20 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_tariff_subscription_payment'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('content', models.CharField(blank=True, max_length=1024)),
                ('links', models.JSONField()),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
    ]