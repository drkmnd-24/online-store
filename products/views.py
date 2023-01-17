# from django.views.generic.detail import DetailView
# from django.views.generic.list import ListView
from django.http import JsonResponse

from .models import Product, Manufacturer


def product_list(request):
    queryset = Product.objects.all()
    data = {"queryset": list(queryset.values())}
    response = JsonResponse(data)

    return response


def product_detail(request, pk):
    try:
        queryset = Product.objects.get(pk=pk)
        data = {"queryset": {
            "name": queryset.name,
            "manufacturer": queryset.manufacturer.name,
            "description": queryset.description,
            "photo": queryset.photo.url,
            "price": queryset.price,
            "shipping_cost": queryset.shipping_cost,
            "quantity": queryset.quantity,
        }}
        response = JsonResponse(data)

    except Product.DoesNotExist:
        response = JsonResponse({"Error": {
            "code": 404,
            "message": "product not found!"
        }}, status=404)
    return response


# class ProductDetailView(DetailView):
#     model = Product
#     template_name = 'products/product_detail.html'
#
#
# class ProductListView(ListView):
#     model = Product
#     template_name = 'products/product_list.html'
