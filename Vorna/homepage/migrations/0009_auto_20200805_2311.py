# Generated by Django 3.0.9 on 2020-08-06 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0008_auto_20200805_2308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currency',
            name='timestamp',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
