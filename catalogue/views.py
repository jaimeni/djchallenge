# Create your views here.
from django.core.paginator import Paginator
from django.http import HttpResponse

from django.template import loader
from django.views.decorators.http import require_http_methods
from rest_framework import viewsets, status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from catalogue.models import Product
from catalogue.serializers import ProductSerializer
from catalogue.utils import format_list, validate_range_price


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class FiltersByPriceListView(ListAPIView):
    queryset = Product.objects.all()

    def get(self, request, *args, **kwargs):
        response = Response()
        value_min = request.data.get('value_min')
        value_max = request.data.get('value_max')
        if validate_range_price(value_min, value_max):
            products = self.queryset.filter(pvp__gte=value_min,
                                            pvp__lte=value_max)
            products = format_list(products)

            response.data = products
            response.status_code = status.HTTP_200_OK
        else:
            response.data = {
                'error': 'The minimum price is lower than maximum price'
            }
            response.status_code = status.HTTP_404_NOT_FOUND
        return response


@require_http_methods(["GET"])
def landing(request):
    product_list = format_list(Product.objects.all())
    paginator = Paginator(product_list, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    template = loader.get_template('catalogue/product_list.html')
    context = {'products': page_obj}
    return HttpResponse(template.render(context, request))
