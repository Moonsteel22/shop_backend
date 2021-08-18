from rest_framework.routers import SimpleRouter

from .views import CartViewSet

app_name = "cart"

router = SimpleRouter()
router.register(r"carts", CartViewSet)

urlpatterns = []

urlpatterns += router.urls
