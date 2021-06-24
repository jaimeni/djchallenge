# Useful functions
from decimal import Decimal


def get_or_none(model, *args, **kwargs):
    try:
        return model.object.get(*args, **kwargs)
    except model.DoesNotExist:
        return None


def format_list(products):
    data = []
    for product in products:
        image = []
        for img in product.details.all():
            image.append(img.image.name)
        data.append({
            'sku': product.sku,
            'name': product.name,
            'description': product.description,
            'category': product.category.name,
            'price': product.pvp,
            'images': image
        })
    return data


def validate_range_price(value_min, value_max):
    try:
        return True if Decimal(value_min) < Decimal(value_max) else False
    except Exception:
        return None

