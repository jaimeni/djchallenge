from django.db import models

from catalogue.models import Category


class Product(models.Model):
    category = models.ForeignKey(
        Category, verbose_name='Category', related_name='Categories',
        null=True, on_delete=models.CASCADE
    )
    sku = models.CharField(
        'SKU', max_length=225, null=False, blank=False, help_text='SKU'
    )
    name = models.CharField(
        'Name', max_length=225, null=False, blank=False, help_text='Name'
    )
    description = models.CharField(
        'Description', max_length=225, null=True, blank=True,
        help_text='Description'
    )
    pvp = models.DecimalField(
        'PVP', max_digits=9, decimal_places=2, null=False, blank=False,
        help_text='Price of sale'
    )

    class Meta:
        ordering = ('name', 'id')
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return '{name}-{sku}'.format(sku=self.name, name=self.sku)


class ProductDetail(models.Model):
    product = models.ForeignKey(
        Product, verbose_name='Product', related_name='details',
        null=True, on_delete=models.CASCADE
    )
    image = models.ImageField(
        'Images', upload_to='product', null=None
    )

    class Meta:
        ordering = ('id', 'product')
        verbose_name = 'Product detail'
        verbose_name_plural = 'Product details'

    def __str__(self):
        return '{product}'.format(product=self.product)
