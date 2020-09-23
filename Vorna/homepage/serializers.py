from rest_framework import serializers
from .models import *


class CurrencyExchangeSerializer(serializers.ModelSerializer):
    """Serilizer for All of Currency rates"""

    class Meta:
        model = CurrencyExchange
        fields = ('id', 'EURUSD', 'GBPUSD', 'AUDUSD', 'USDCAD', 'USDJPY',
                  'USDINR', 'USDTRY', 'USDCNY', 'USDRUB', 'USDAED', 'timestamp')
        read_only_fields = ('id', )


class ForexExchangeSerializer(serializers.ModelSerializer):
    """Serializer class for ForexExchange model"""

    class Meta:
        model = ForexExchange
        fields = ('id', 'forex_rates', 'timestamp')
        read_only_fields = ('id',)


class InvestingProductSerializer(serializers.ModelSerializer):
    """ Serializer class for Investing Products """

    class Meta:
        model = InvestingProduct
        fields = ('id', 'products', 'timestamp')
        read_only_fields = ('id',)


class InvestingStockSerializer(serializers.ModelSerializer):
    """ Serializer class for Investing Products """

    class Meta:
        model = InvestingStock
        fields = ('id', 'stock', 'timestamp')
        read_only_fields = ('id',)


class MexExchangeSerializer(serializers.ModelSerializer):
    """ Serializer class for Mex exchange rates """

    class Meta:
        model = MexExchange
        fields = ('id', 'exchange_rate', 'timestamp')
        read_only_fields = ('id',)
