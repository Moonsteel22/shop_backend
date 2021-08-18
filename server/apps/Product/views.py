from server.apps.product.serializers import ProductSerializer
from server.apps.product.models import Product
from rest_framework.viewsets import ModelViewSet

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
