from rest_framework import serializers
from .models import Cart



class CartSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Cart

    def create(self, validated_data):
        try:
            user_product = Cart.objects.filter(user_id=validated_data['user_id'])
            user_product = user_product.get(
                product_id=validated_data['product_id'])
            if 'amount' in validated_data:
                user_product.amount += validated_data['amount']
            else:
                user_product.amount += 1
            user_product.save()
            return user_product
        except Exception:
            new_cart_element = Cart.objects.create(**validated_data)
            return new_cart_element
