from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'list': 'api/products'
    }
    return Response(api_urls)

@api_view(['GET'])
def getAllProducts(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)