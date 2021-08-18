from server.apps.Product.models import Product
from django.db import models
from django.db.models.deletion import CASCADE
from server.apps.User.models import User

class Cart(models.Model):
    user_id = models.ForeignKey(User, on_delete=CASCADE)
    product_id = models.ForeignKey(Product,on_delete=CASCADE)
    amount = models.PositiveIntegerField(default=1)
