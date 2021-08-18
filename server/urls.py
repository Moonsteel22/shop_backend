from django.contrib import admin
from django.urls import include
from django.urls import path

from .apps.user import urls as user_urls
from .apps.product import urls as product_urls
from .apps.cart import urls as cart_urls
urlpatterns = [
    path("api/", include(user_urls, namespace="user")),
    path("api/", include(product_urls, namespace="product")),
    path("api/", include(cart_urls, namespace="cart")),
    path("admin/", admin.site.urls),
]
