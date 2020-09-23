from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
# router.register('EURtoUSD', views.EURtoUSDViewSet, basename="EURtoUSD")
# router.register('GBPtoUSD', views.GBPtoUSDViewSet, basename="GBPtoUSD")
# router.register('AUDtoUSD', views.AUDtoUSDViewSet, basename="AUDtoUSD")
# router.register('USDtoCAD', views.USDtoCADViewSet, basename="USDtoCAD")
# router.register('USDtoJPY', views.USDtoJPYViewSet, basename="USDtoJPY")
# router.register('USDtoINR', views.USDtoINRViewSet, basename="USDtoINR")
# router.register('USDtoTRY', views.USDtoTRYViewSet, basename="USDtoTRY")
# router.register('USDtoCNY', views.USDtoCNYViewSet, basename="USDtoCNY")
# router.register('USDtoRUB', views.USDtoRUBViewSet, basename="USDtoRUB")
# router.register('USDtoAED', views.USDtoAEDViewSet, basename="USDtoAED")
router.register("CurrencyExchange",
                views.CurrencyExchangeViewSet, basename='CurrencyExchange')
router.register("ForexExchange",
                views.ForexExchangeViewSet, basename='ForexExchange')
router.register("product",
                views.InvestingProductViewSet, basename='productExchange')
router.register("stock",
                views.InvestingStockViewSet, basename='stockExchange')
router.register("exchangeIR",
                views.MexExchangeViewSet, basename='exchangeIR')
router.register("gold",
                views.GoldPriceViewSet, basename='gold')


urlpatterns = [
    path('', views.home, name='home'),
    path('update/', include(router.urls)),
    path('update/final', views.AllRatesViewSet.as_view(), basename='final')
]
