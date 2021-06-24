from rest_framework.serializers import ModelSerializer

from catalogue.models import Category, Product
from catalogue.utils import get_or_none


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'description')


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'sku', 'name', 'description', 'pvp', 'category')

    def save(self, **kwargs):
        self.validated_data["category"] = get_or_none(
            Category, **self.validated_data["category"]
        )
        return super(ProductSerializer, self).save(**kwargs)


class ProductDetailSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'product', 'image')

    def save(self, **kwargs):
        self.validated_data["product"] = get_or_none(
            Product, **self.validated_data["product"]
        )
        return super(ProductDetailSerializer, self).save(**kwargs)
