# Generated by Django 3.1 on 2020-09-12 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0011_audtousd_gbptousd_usdtoaed_usdtocad_usdtocny_usdtoinr_usdtojpy_usdtorub_usdtotry'),
    ]

    operations = [
        migrations.CreateModel(
            name='CurrencyExchange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EURUSD', models.DecimalField(decimal_places=10, max_digits=20)),
                ('GBPUSD', models.DecimalField(decimal_places=10, max_digits=20)),
                ('AUDUSD', models.DecimalField(decimal_places=10, max_digits=20)),
                ('USDCAD', models.DecimalField(decimal_places=10, max_digits=20)),
                ('USDJPY', models.DecimalField(decimal_places=10, max_digits=20)),
                ('USDINR', models.DecimalField(decimal_places=10, max_digits=20)),
                ('USDTRY', models.DecimalField(decimal_places=10, max_digits=20)),
                ('USDCNY', models.DecimalField(decimal_places=10, max_digits=20)),
                ('USDRUB', models.DecimalField(decimal_places=10, max_digits=20)),
                ('USDAED', models.DecimalField(decimal_places=10, max_digits=20)),
                ('timestamp', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='AUDtoUSD',
        ),
        migrations.DeleteModel(
            name='EURtoUSD',
        ),
        migrations.DeleteModel(
            name='GBPtoUSD',
        ),
        migrations.DeleteModel(
            name='USDtoAED',
        ),
        migrations.DeleteModel(
            name='USDtoCAD',
        ),
        migrations.DeleteModel(
            name='USDtoCNY',
        ),
        migrations.DeleteModel(
            name='USDtoINR',
        ),
        migrations.DeleteModel(
            name='USDtoJPY',
        ),
        migrations.DeleteModel(
            name='USDtoRUB',
        ),
        migrations.DeleteModel(
            name='USDtoTRY',
        ),
    ]
