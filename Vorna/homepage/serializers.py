from rest_framework import serializers
from .models import *


class CurrencySerializer(serializers.ModelSerializer):
    """Serializer for Currency object"""

    class Meta:
        model = Currency
        fields = ('id', 'sname', 'fname', 'value')
        read_only_fields = ('id',)
        
        
    def create(self, validated_data):
        name = validated_data.get("sname", None)
        full_name = validated_data.get("fname", None)
        price = validated_data.get("value", None)
        deft = {
            'fname' : full_name,
            'value' : price
            }
        obj, created = Currency.objects.update_or_create(sname=name,
                                                defaults=deft)
        return obj
        
        
class EURtoUSDSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = EURtoUSD
        fields = ('id', 'rate', 'timestamp')
        read_only_fields = ('id',)
        
        
class GBPtoUSDSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = GBPtoUSD
        fields = ('id', 'rate', 'timestamp')
        read_only_fields = ('id',)
               
        
class AUDtoUSDSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = AUDtoUSD
        fields = ('id', 'rate', 'timestamp')
        read_only_fields = ('id',)
                
        
class USDtoCADSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = USDtoCAD
        fields = ('id', 'rate', 'timestamp')
        read_only_fields = ('id',)
                
        
class USDtoJPYSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = USDtoJPY
        fields = ('id', 'rate', 'timestamp')
        read_only_fields = ('id',)
                
        
class USDtoINRSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = USDtoINR
        fields = ('id', 'rate', 'timestamp')
        read_only_fields = ('id',)
                
        
class USDtoTRYSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = USDtoTRY
        fields = ('id', 'rate', 'timestamp')
        read_only_fields = ('id',)
                
        
class USDtoCNYSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = USDtoCNY
        fields = ('id', 'rate', 'timestamp')
        read_only_fields = ('id',)
                
        
class USDtoRUBSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = USDtoRUB
        fields = ('id', 'rate', 'timestamp')
        read_only_fields = ('id',)
                
        
class USDtoAEDSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = USDtoAED
        fields = ('id', 'rate', 'timestamp')
        read_only_fields = ('id',)
