# Generated by Django 3.1 on 2020-09-18 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0012_auto_20200912_1243'),
    ]

    operations = [
        migrations.CreateModel(
            name='ForexExchange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forex_rates', models.JSONField()),
                ('timestamp', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]
