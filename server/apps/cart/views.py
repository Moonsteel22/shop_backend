from server.apps.cart.serializers import CartSerializer
from server.apps.cart.models import Cart
from rest_framework.viewsets import ModelViewSet

class CartViewSet(ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer