from server.apps.Product.serializers import ProductSerializer
from server.apps.Product.models import Product
from rest_framework.viewsets import ModelViewSet

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer