from django.db import models
from django.utils import timezone
# Create your models here.

class Currency(models.Model):
    """Model for Currencies exchanges.
       When Updated, a copy should be placed on to the corresponding database
       For Exampled if USD/EUR is updated a copy should be placed in USDtoEUR database."""
    base_currency = models.CharField(max_length=255)
    non_base_currency = models.CharField(max_length=255)
    value = models.DecimalField(max_digits=20, decimal_places=8)
    timestamp = models.DateTimeField(auto_now=True, blank=True, null=True)


class Currency_base(models.Model):
    """Base model for currency tables."""
    rate = models.DecimalField(max_digits=25, decimal_places=10)
    timestamp = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        abstract = True

class CurrencyExchange(models.Model):
    """Currency Exchange rates."""
    EURUSD = models.DecimalField(max_digits=20, decimal_places=10)
    GBPUSD = models.DecimalField(max_digits=20, decimal_places=10)
    AUDUSD = models.DecimalField(max_digits=20, decimal_places=10)
    USDCAD = models.DecimalField(max_digits=20, decimal_places=10)
    USDJPY = models.DecimalField(max_digits=20, decimal_places=10)
    USDINR = models.DecimalField(max_digits=20, decimal_places=10)
    USDTRY = models.DecimalField(max_digits=20, decimal_places=10)
    USDCNY = models.DecimalField(max_digits=20, decimal_places=10)
    USDRUB = models.DecimalField(max_digits=20, decimal_places=10)
    USDAED = models.DecimalField(max_digits=20, decimal_places=10)
    timestamp = models.DateTimeField(auto_now=True, blank=True, null=True)


class ForexExchange(models.Model):
    """ Exchange rates from ForexFactory """

    forex_rates = models.JSONField()
    timestamp = models.DateTimeField(auto_now=True, blank=True, null=True)


class InvestingProduct(models.Model):
    """ Product rates from Investing """

    products = models.JSONField()
    timestamp = models.DateTimeField(auto_now=True, blank=True, null=True)


class InvestingStock(models.Model):
    """ Product rates from Investing """

    stock = models.JSONField()
    timestamp = models.DateTimeField(auto_now=True, blank=True, null=True)


class MexExchange(models.Model):
    """ Currency exchange rates from mex """

    exchange_rate = models.JSONField()
    timestamp = models.DateTimeField(auto_now=True, blank=True, null=True)


class GoldPrice(models.Model):
    """ Gold exchange rates """

    gold = models.JSONField()
    timestamp = models.DateTimeField(auto_now=True, blank=True, null=True)
