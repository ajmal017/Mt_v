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


class CurrencyViewSet(generics.ListCreateAPIView, viewsets.GenericViewSet):
    """Manage Currency add or get"""

    # authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Currency.objects.all()
    serializer_class = serializers.CurrencySerializer


class ExchangeBaseClass(generics.ListCreateAPIView, viewsets.GenericViewSet, mixins.CreateModelMixin):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)


    @action(methods=['GET'], permission_classes=[IsAuthenticatedOrReadOnly], url_path='latest', detail=False)
    def get_latest(self, request, pk=None):
        latest = self.serializer_class.Meta.model.objects.last()
        serializer = self.serializer_class(latest)
        return Response(serializer.data)


class EURtoUSDViewSet(ExchangeBaseClass):
    queryset = EURtoUSD.objects.all()
    serializer_class = serializers.EURtoUSDSerializer


class GBPtoUSDViewSet(ExchangeBaseClass):
    queryset = GBPtoUSD.objects.all()
    serializer_class = serializers.GBPtoUSDSerializer


class AUDtoUSDViewSet(ExchangeBaseClass):
    queryset = AUDtoUSD.objects.all()
    serializer_class = serializers.AUDtoUSDSerializer


class USDtoCADViewSet(ExchangeBaseClass):
    queryset = USDtoCAD.objects.all()
    serializer_class = serializers.USDtoCADSerializer


class USDtoJPYViewSet(ExchangeBaseClass):
    queryset = USDtoJPY.objects.all()
    serializer_class = serializers.USDtoJPYSerializer


class USDtoINRViewSet(ExchangeBaseClass):
    queryset = USDtoINR.objects.all()
    serializer_class = serializers.USDtoINRSerializer


class USDtoTRYViewSet(ExchangeBaseClass):
    queryset = USDtoTRY.objects.all()
    serializer_class = serializers.USDtoTRYSerializer


class USDtoCNYViewSet(ExchangeBaseClass):
    queryset = USDtoCNY.objects.all()
    serializer_class = serializers.USDtoCNYSerializer


class USDtoRUBViewSet(ExchangeBaseClass):
    queryset = USDtoRUB.objects.all()
    serializer_class = serializers.USDtoRUBSerializer


class USDtoAEDViewSet(ExchangeBaseClass):
    queryset = USDtoAED.objects.all()
    serializer_class = serializers.USDtoAEDSerializer


class AllCurrencyViewSet(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get(self, request, pk=None):
        eurusd = EURtoUSD.objects.last()
        gbpusd = GBPtoUSD.objects.last()

        context = {
            "request": request,
        }

        usd_serializer = serializers.EURtoUSDSerializer(eurusd, context=context)
        gbp_serializer = serializers.GBPtoUSDSerializer(gbpusd, context=context)

        response = usd_serializer + gbp_serializer

        return Response(response)
