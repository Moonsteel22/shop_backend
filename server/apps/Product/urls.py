from rest_framework.routers import SimpleRouter

from .views import ProductViewSet

app_name = "products"

router = SimpleRouter()
router.register(r"products", ProductViewSet)

urlpatterns = []

urlpatterns += router.urls
