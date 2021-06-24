import math
from decimal import Decimal

from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField

from catalogue.models import Category, Product, ProductDetail
from catalogue.utils import get_or_none


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'description')


class ProductDetailSerializer(ModelSerializer):
    class Meta:
        model = ProductDetail
        fields = ('id', 'product', 'image')

    def save(self, **kwargs):
        self.validated_data["product"] = get_or_none(
            Product, **self.validated_data["product"]
        )
        return super(ProductDetailSerializer, self).save(**kwargs)


class ProductSerializer(ModelSerializer):
    details = ProductDetailSerializer(many=True)

    class Meta:
        model = Product
        fields = ('id', 'sku', 'name', 'description', 'pvp', 'category',
                  'details')

    def save(self, **kwargs):
        self.validated_data["category"] = get_or_none(
            Category, **self.validated_data["category"]
        )
        self.validated_data["pvp"] = math.fabs(
            Decimal(self.validated_data["pvp"]))
        return super(ProductSerializer, self).save(**kwargs)
