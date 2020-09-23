from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, mixins, views, status, generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.decorators import api_view, action

from .models import *

from homepage import serializers

news = [
        {
            'title': 'test',
            'text': 'test 1 for news. Lurem ipsom or something idk.',
            'link': '#'
        },
        {
            'title': 'test2',
            'text': 'test 2 for news. Lurem ipsom or something idk.',
            'link': '#'
        },
        {
            'title': 'test3',
            'text': 'test 2 for news. Lurem ipsom or something idk.',
            'link': '#'
        },
        {
            'title': 'test4',
            'text': 'test 2 for news. Lurem ipsom or something idk.',
            'link': '#'
        }

]


# Create your views here.
def home(request):
    context = {
        'news': news,
        'title': 'Vorna - Homepage'
        }
    return render(request, 'homepage/index.html', context)
    # return HttpResponse('<h1>Blog Home</h1>')


class ViewBase(generics.ListCreateAPIView, viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated,)

    @action(methods=['GET'], permission_classes=[IsAuthenticatedOrReadOnly], url_path='latest', detail=False)
    def get_latest(self, request, pk=None):
        latest = self.serializer_class.Meta.model.objects.last()
        serializer = self.serializer_class(latest)
        return Response(serializer.data)


class CurrencyExchangeViewSet(generics.ListCreateAPIView, viewsets.GenericViewSet):
    # authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = CurrencyExchange.objects.all()
    serializer_class = serializers.CurrencyExchangeSerializer

    @action(methods=['GET'], permission_classes=[IsAuthenticatedOrReadOnly], url_path='latest', detail=False)
    def get_latest(self, request, pk=None):
        latest = CurrencyExchange.objects.last()
        serializer = self.serializer_class(latest)
        return Response(serializer.data)


class ForexExchangeViewSet(ViewBase):
    # authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = ForexExchange.objects.all()
    serializer_class = serializers.ForexExchangeSerializer


class InvestingProductViewSet(ViewBase):
    queryset = InvestingProduct.objects.all()
    serializer_class = serializers.InvestingProductSerializer


class InvestingStockViewSet(ViewBase):
    queryset = InvestingStock.objects.all()
    serializer_class = serializers.InvestingStockSerializer


class MexExchangeViewSet(ViewBase):
    queryset = MexExchange.objects.all()
    serializer_class = serializers.MexExchangeSerializer


class GoldPriceViewSet(ViewBase):
    queryset = GoldPrice.objects.all()
    serializer_class = serializers.GoldPriceSerializer
