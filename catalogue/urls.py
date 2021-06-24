from django.urls import path
from rest_framework import routers

from catalogue.views import ProductViewSet, landing, FiltersByPriceListView

app_name = 'catalogue'

router = routers.DefaultRouter()

router.register(r'product', ProductViewSet, basename='product')

urlpatterns = [
    path('', landing, name='landing'),
    path('filter-by-price', FiltersByPriceListView.as_view(),
         name='filter-by-price'),
]

urlpatterns += router.urls
