from rest_framework.routers import SimpleRouter

from .views import CatalogueViewSet

app_name = "user"

router = SimpleRouter()
router.register(r"catalogue", CatalogueViewSet.as_view())

urlpatterns = []

urlpatterns += router.urls
