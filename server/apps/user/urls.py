from rest_framework.routers import SimpleRouter

from .views import UserViewSet

app_name = "user"

router = SimpleRouter()
router.register(r"users", UserViewSet)

urlpatterns = []

urlpatterns += router.urls
